import torch as th
import librosa as rosa

import audioreactive as ar
from  generate_audiovisual import generate

#OVERRIDE = dict(audio_file="data/audio/coding_chaos_test_track.wav", out_size=896)
BPM = 130


def initialize(args):
    # exercise for the reader:
    # install https://github.com/deezer/spleeter
    # split your audio file into 4 tracks
    # then load them individually for higher-quality onsets/chroma/etc. e.g.:
    #     !spleeter separate $audio_file -p spleeter:4stems
    #     drums, drum_sr = rosa.load("/path/to/drum_file.wav")

    print("finding onsets...")

    # args.drum_onsets = ar.onsets(args.audio, args.sr, args.n_frames, fmax=150, smooth=5, clip=97, power=2)
    # args.bass_onsets = ar.onsets(args.audio, args.sr, args.n_frames, fmin=150, fmax=500, smooth=5, clip=99, power=2)
    # args.piano_onsets = ar.onsets(args.audio, args.sr, args.n_frames, fmin=500, smooth=5, clip=99, power=2)
    # ar.plot_signals([args.drum_onsets, args.bass_onsets, args.piano_onsets])

    audio_dir = "data/audio/night_is_young/"

    audio, sr = rosa.load(audio_dir + "KICK.wav", offset=args.offset, duration=args.duration)
    args.kick_onsets = ar.onsets(audio, sr, args.n_frames, margin=1, smooth=2, power=1,clip=99)
    
    audio, sr = rosa.load(audio_dir + "SNARE_BOTTOM.wav", offset=args.offset, duration=args.duration)
    args.snare_onsets = ar.onsets(audio, sr, args.n_frames, margin=1, smooth=1, power=1, clip=99)

    audio, sr = rosa.load(audio_dir + "KIT_OH.wav", offset=args.offset, duration=args.duration)
    drum_onsets = ar.onsets(audio, sr, args.n_frames, margin=1, smooth=2, power=1, clip=95)
    args.drum_onsets = drum_onsets

    #args.kick_onsets = th.zeros_like(drum_onsets)
    #args.snare_onsets = th.zeros_like(drum_onsets)
    #args.drum_onsets = th.fmax(drum_onsets, th.fmax(args.kick_onsets, args.snare_onsets))

    audio, sr = rosa.load(audio_dir + "BASS_DI.wav", offset=args.offset, duration=args.duration)
    args.bass_onsets = ar.onsets(audio, sr, args.n_frames, margin=8, smooth=1, power=1, fmin=30, clip=95)

    audio, sr = rosa.load(audio_dir + "PNO.wav", offset=args.offset, duration=args.duration)
    args.piano_onsets = ar.onsets(audio, sr, args.n_frames, smooth=1, clip=96, power=1, margin=4, fmin=500)

    print("done onsets")

    ar.plot_signals([args.kick_onsets, args.snare_onsets, drum_onsets, args.drum_onsets, args.bass_onsets, 
                     args.piano_onsets])
    
    return args


def spline_latents(selection, args):
    latents = ar.spline_loops(selection, args.n_frames, 1, loop=False)
    #latents = ar.gaussian_filter(latents.float(), 3, causal=0.1)
    return latents

def get_latents(selection, args):
    return spline_latents(selection, args)

def get_latents_template(selection, args):
    # selection = [num of latents in selection/file, n_latent=14, latent_dim=512]

    #latents = ar.slerp_loops(selection, args.n_frames, 2, smoothing=1, loop=False) #spring
    latents = ar.spline_loops(selection, args.n_frames, 1, loop=False) # fall

    drum_onsets = args.drum_onsets[:, None, None]
    bass_onsets = args.bass_onsets[:, None, None]
    piano_onsets = args.piano_onsets[:, None, None]
    #print(selection.shape, latents.shape, lo_onsets.shape, hi_onsets.shape)
    #breakpoint()

    # use onsets to modulate towards latents
    # drum = 4, bass = 1, piano = 6
    n_latent = selection.shape[1]

    # a = 1
    # L = th.randint(0, n_latent, (1,)).item() # use torch rand so seeding is less complicated
    # latents = a * drum_onsets * selection[[L]] + (1 - a * drum_onsets) * latents

    # a = 1
    # L = th.randint(0, n_latent, (1,)).item()
    # latents = a * bass_onsets * selection[[L]] + (1 - a * bass_onsets) * latents

    # a = 1
    # L = th.randint(0, n_latent, (1,)).item()
    # latents = a * piano_onsets * selection[[L]] + (1 - a * piano_onsets) * latents
    
    latents = ar.gaussian_filter(latents.float(), 3, causal=0.1)

    return latents

def bass_solo_noise(height, width, scale, num_scales, args):
    if width > 512:  # larger sizes don't fit in VRAM, just use default or randomize
        return None

    drum_onsets = args.drum_onsets[:, None, None, None].cuda()
    bass_onsets = args.bass_onsets[:, None, None, None].cuda()
    piano_onsets = args.piano_onsets[:, None, None, None].cuda()

    # create noise which changes quickly (small standard deviation smoothing)
    noise_noisy = ar.gaussian_filter(th.randn((args.n_frames, 1, height, width), device="cuda"), 5)

    # create noise which changes slowly (large standard deviation smoothing)
    noise = ar.gaussian_filter(th.randn((args.n_frames, 1, height, width), device="cuda"), 106)

    # for lower layers, noise is affected by bass
    if width < 64:
        a = 1
        noise = a * bass_onsets * noise_noisy + (1 - a * bass_onsets) * noise
    # middle layers affected by drums
    if width > 16 and width < 128:
        a = 0.65
        noise = a * drum_onsets * noise_noisy + (1 - a * drum_onsets) * noise
    # for upper layers, noise is affected by piano
    if width > 32:
        a = 0.8
        noise = a * piano_onsets * noise_noisy + (1 - a * piano_onsets) * noise

    # ensure amplitude of noise is close to standard normal distribution (dividing by std. dev. gets it exactly there)
    noise /= noise.std() * 2

    noise = ar.gaussian_filter(noise, 2, causal=0.2)

    return noise.cpu()

def drum_noise(height, width, scale, num_scales, args):
    if width > 512:  # larger sizes don't fit in VRAM, just use default or randomize
        return None

    drum_onsets = args.drum_onsets[:, None, None, None].cuda()
    snare_onsets = args.snare_onsets[:, None, None, None].cuda()

    # create noise which changes quickly (small standard deviation smoothing)
    noise_noisy = ar.gaussian_filter(th.randn((args.n_frames, 1, height, width), device="cuda"), 5)

    # create noise which changes slowly (large standard deviation smoothing)
    noise = ar.gaussian_filter(th.randn((args.n_frames, 1, height, width), device="cuda"), 120)

    #if width < 64:
    a = 1
    noise = a * drum_onsets * noise_noisy + (1 - a * drum_onsets) * noise
    #if width > 64:
    #    a = 1
    #    noise = a * snare_onsets * noise_noisy + (1 - a * snare_onsets) * noise

    # ensure amplitude of noise is close to standard normal distribution (dividing by std. dev. gets it exactly there)
    noise /= noise.std() * 1.5

    return noise.cpu()

def mixed_noise(height, width, scale, num_scales, args):
    if width > 512:  # larger sizes don't fit in VRAM, just use default or randomize
        return None

    drum_onsets = args.drum_onsets[:, None, None, None].cuda()
    bass_onsets = args.bass_onsets[:, None, None, None].cuda()
    piano_onsets = args.piano_onsets[:, None, None, None].cuda()

    noise_noisy = ar.gaussian_filter(th.randn((args.n_frames, 1, height, width), device="cuda"), 5)
    noise = ar.gaussian_filter(th.randn((args.n_frames, 1, height, width), device="cuda"), 200)

    if width < 64:
        a = 0.75
        noise = a * drum_onsets * noise_noisy + (1 - a * drum_onsets) * noise
    if width > 16 and width < 128:
        a = 0.75
        noise = a * bass_onsets * noise_noisy + (1 - a * bass_onsets) * noise
    if width > 32:
        a = 0.75
        noise = a * piano_onsets * noise_noisy + (1 - a * piano_onsets) * noise

    noise /= noise.std() * 1.5
    noise = ar.gaussian_filter(noise, 2, causal=0.2)
    return noise.cpu()

def mixed_opening_noise(height, width, scale, num_scales, args):
    if width > 512:  # larger sizes don't fit in VRAM, just use default or randomize
        return None

    drum_onsets = args.drum_onsets[:, None, None, None].cuda()
    bass_onsets = args.bass_onsets[:, None, None, None].cuda()
    piano_onsets = args.piano_onsets[:, None, None, None].cuda()

    noise_noisy = ar.gaussian_filter(th.randn((args.n_frames, 1, height, width), device="cuda"), 5)
    noise = ar.gaussian_filter(th.randn((args.n_frames, 1, height, width), device="cuda"), 200)

    if width < 64:
        a = 1
        noise = a * drum_onsets * noise_noisy + (1 - a * drum_onsets) * noise
    if width > 16 and width < 128:
        a = 0.5
        noise = a * bass_onsets * noise_noisy + (1 - a * bass_onsets) * noise
    if width > 32:
        a = 0.5
        noise = a * piano_onsets * noise_noisy + (1 - a * piano_onsets) * noise

    noise /= noise.std() * 1.5
    noise = ar.gaussian_filter(noise, 2, causal=0.2)
    return noise.cpu()

def mixed_iris_moon_noise(height, width, scale, num_scales, args):
    if width > 512:  # larger sizes don't fit in VRAM, just use default or randomize
        return None

    drum_onsets = args.drum_onsets[:, None, None, None].cuda()
    bass_onsets = args.bass_onsets[:, None, None, None].cuda()
    piano_onsets = args.piano_onsets[:, None, None, None].cuda()

    noise_noisy = ar.gaussian_filter(th.randn((args.n_frames, 1, height, width), device="cuda"), 5)
    noise = ar.gaussian_filter(th.randn((args.n_frames, 1, height, width), device="cuda"), 200)

    if width < 64:
        a = 0.8
        noise = a * drum_onsets * noise_noisy + (1 - a * drum_onsets) * noise
    if width > 16 and width < 128:
        a = 0.8
        noise = a * bass_onsets * noise_noisy + (1 - a * bass_onsets) * noise
    if width > 32:
        a = 0.8
        noise = a * piano_onsets * noise_noisy + (1 - a * piano_onsets) * noise

    noise /= noise.std() * 1.5
    noise = ar.gaussian_filter(noise, 2, causal=0.2)
    return noise.cpu()

def bass_solo_noise(height, width, scale, num_scales, args):
    if width > 512:  # larger sizes don't fit in VRAM, just use default or randomize
        return None

    drum_onsets = args.drum_onsets[:, None, None, None].cuda()
    bass_onsets = args.bass_onsets[:, None, None, None].cuda()
    piano_onsets = args.piano_onsets[:, None, None, None].cuda()

    noise_noisy = ar.gaussian_filter(th.randn((args.n_frames, 1, height, width), device="cuda"), 5)
    noise = ar.gaussian_filter(th.randn((args.n_frames, 1, height, width), device="cuda"), 200)

    if width < 64:
        a = 1
        noise = a * bass_onsets * noise_noisy + (1 - a * bass_onsets) * noise
    if width > 16 and width < 128:
        a = 0.8
        noise = a * drum_onsets * noise_noisy + (1 - a * drum_onsets) * noise
    if width > 32:
        a = 0.5
        noise = a * piano_onsets * noise_noisy + (1 - a * piano_onsets) * noise

    noise /= noise.std() * 2
    noise = ar.gaussian_filter(noise, 3, causal=0.2)
    return noise.cpu()

def piano_drum_noise(height, width, scale, num_scales, args):
    if width > 512:  # larger sizes don't fit in VRAM, just use default or randomize
        return None

    piano_onsets = args.piano_onsets[:, None, None, None].cuda()
    drum_onsets = args.drum_onsets[:, None, None, None].cuda()

    noise_noisy = ar.gaussian_filter(th.randn((args.n_frames, 1, height, width), device="cuda"), 5)
    noise = ar.gaussian_filter(th.randn((args.n_frames, 1, height, width), device="cuda"), 200)

    if width < 64:
        a = 1
        noise = a * piano_onsets * noise_noisy + (1 - a * piano_onsets) * noise
    if width > 32:
        a = 0.75
        noise = a * drum_onsets * noise_noisy + (1 - a * drum_onsets) * noise

    noise /= noise.std() * 1.5
    noise = ar.gaussian_filter(noise, 2, causal=0.2)
    return noise.cpu()

def bass_drum_noise(height, width, scale, num_scales, args):
    if width > 512:  # larger sizes don't fit in VRAM, just use default or randomize
        return None

    bass_onsets = args.bass_onsets[:, None, None, None].cuda()
    drum_onsets = args.drum_onsets[:, None, None, None].cuda()

    noise_noisy = ar.gaussian_filter(th.randn((args.n_frames, 1, height, width), device="cuda"), 5)
    noise = ar.gaussian_filter(th.randn((args.n_frames, 1, height, width), device="cuda"), 200)

    if width < 64:
        a = 1
        noise = a * bass_onsets * noise_noisy + (1 - a * bass_onsets) * noise
    if width > 32:
        a = 0.75
        noise = a * drum_onsets * noise_noisy + (1 - a * drum_onsets) * noise

    noise /= noise.std() * 1.5
    noise = ar.gaussian_filter(noise, 2, causal=0.2)
    return noise.cpu()


def nebula_ending_noise(height, width, scale, num_scales, args):
    if width > 512:  # larger sizes don't fit in VRAM, just use default or randomize
        return None

    drum_onsets = args.drum_onsets[:, None, None, None].cuda()
    bass_onsets = args.bass_onsets[:, None, None, None].cuda()
    piano_onsets = args.piano_onsets[:, None, None, None].cuda()

    noise_noisy = ar.gaussian_filter(th.randn((args.n_frames, 1, height, width), device="cuda"), 5)
    noise = ar.gaussian_filter(th.randn((args.n_frames, 1, height, width), device="cuda"), 200)

    if width < 64:
        a = 1
        noise = a * bass_onsets * noise_noisy + (1 - a * bass_onsets) * noise
    if width > 16 and width < 128:
        a = 1
        noise = a * piano_onsets * noise_noisy + (1 - a * piano_onsets) * noise
    if width > 32:
        a = 1
        noise = a * drum_onsets * noise_noisy + (1 - a * drum_onsets) * noise

    noise /= noise.std() * 2
    noise = ar.gaussian_filter(noise, 3, causal=0.2)
    return noise.cpu()


def get_noise(height, width, scale, num_scales, args):
    return nebula_ending_noise(height, width, scale, num_scales, args)


def get_noise_template(height, width, scale, num_scales, args):
    if width > 512:  # larger sizes don't fit in VRAM, just use default or randomize
        return None

    drum_onsets = args.drum_onsets[:, None, None, None].cuda()
    bass_onsets = args.bass_onsets[:, None, None, None].cuda()
    piano_onsets = args.piano_onsets[:, None, None, None].cuda()

    # create noise which changes quickly (small standard deviation smoothing)
    noise_noisy = ar.gaussian_filter(th.randn((args.n_frames, 1, height, width), device="cuda"), 5)

    # create noise which changes slowly (large standard deviation smoothing)
    noise = ar.gaussian_filter(th.randn((args.n_frames, 1, height, width), device="cuda"), 200)

    # for lower layers, noise is affected by bass
    if width < 64:
        a = 1
        noise = a * bass_onsets * noise_noisy + (1 - a * bass_onsets) * noise
    # middle layers affected by drums
    if width > 16 and width < 128:
        a = 0.7
        noise = a * drum_onsets * noise_noisy + (1 - a * drum_onsets) * noise
    # for upper layers, noise is affected by piano
    if width > 32:
        a = 0.7
        noise = a * piano_onsets * noise_noisy + (1 - a * piano_onsets) * noise

    # ensure amplitude of noise is close to standard normal distribution (dividing by std. dev. gets it exactly there)
    noise /= noise.std() * 1.5

    noise = ar.gaussian_filter(noise, 2, causal=0.2)

    print("get noise", height, width, scale, num_scales, noise.shape)

    return noise.cpu()


# def get_bends(args):
#     print("get bends")
#     transform = th.nn.Sequential(
#         th.nn.ReplicationPad2d((2, 2, 0, 0)), ar.AddNoise(0.025 * th.randn(size=(1, 1, 4, 8), device="cuda")),
#     )
#     return [{"layer": 0, "transform": transform}]



if __name__ == "main":
    # you want to set the batch size and ffmpeg_preset as large and as slow as your GPU can handle
    # larger batches => faster, slower preset => smaller + better quality video files
    generate(
        ckpt="model_checkpoints/animal_drums_044000.pt",
        audio_file=OVERRIDE.audio_file,
        output_dir="output/animal_drums/",
        out_size=512, # at the moment only 512x512, 1024x1024, 1920x1080 outputs are supported (out_size = 512, 1024, or 1920 respectively)
        G_res=512,
        batch=4,  # CUDA out of memory errors => smaller batch (also try running the previous cell, to clear some GPU memory)
        ffmpeg_preset="faster",  # RAM crashes => faster preset (see https://trac.ffmpeg.org/wiki/Encode/H.264)
        fps=24,
        duration=60, # remove this line for full video
        initialize=initialize,
        get_latents=get_latents,
        get_noise=get_noise,
        # get_bends=get_bends, # if you're running a 1024px network you can uncomment this for 1920x1080 output
    )