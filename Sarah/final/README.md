# Hot Bod

Composer: **Sarah Thawer** 

Arranger: **Mason Victoria**

When I asked Sarah what sort of visuals she was interested in and showed her some examples of what I had done before, she gravitated to the bold, bright colors and intense visuals of Mason's piece _Source Activate_ in the [Coding Chaos](https://file+.vscode-resource.vscode-webview.net/home/ryankelln/Documents/Projects/Active/ryankelln.com/www/content/project/(http://www.ryankelln.com/project/coding-chaos/)) concert.

That set the tone and when Sarah wanted her piece to investigate the interplay between people's multiple persona's, roles and how others perceive them, I hoped to explore that through the interplay of animal, insect and flower colouring and the interacting dynamics of sexual display, camouflage and identity.

I was really fortunate that my good friend and photographer [Andrew Drown](https://drown.photography/) has been working on a series about rhododendrons and shared his in-progress photographs with me. I'm a huge fan of his work; both of us love interesting textures.

The piece was strongly inspired by Sarah's dynamic playing. More than anything the bold dynamism I hoped to achieve with the piece is a reflection of her personal playing style. As a fan of the look of [Boccioni's Dynamist paintings](https://en.wikipedia.org/wiki/Umberto_Boccioni) I hoped to evoke the movement and color that Sarah incorporates into her playing.

Underlying the fun and beauty of the textures is a question about identity. If the environment is determinant of your identity, who or what is the self when your environment changes around you? For social animals like humans, your identity may move more or less fluidly in reaction to those around you. I question a singular true self, instead an amalgam and continuum of the communities one belongs to and one's degree of identity flexibility. In this piece, the instruments take on the shifting selves, each still evoking the persona of the musician while assuming a variety of textures.

The challenge for the animal textures was that [Optex](https://github.com/RKelln/OptimalTextures/tree/video), the best project to combine the musician images with animal textures, didn't support video and I lacked the time to fix that. Plus I wanted to be able to smoothly interpolate between textures and mix them, so instead I took video stills of the musicians, texturized them with Optex then trained a SWAGAN generator on those. Finally I brought the GAN into [maua-stylegan2](https://github.com/JCBrouwer/maua-stylegan2) to make it audio-reactive. Like in _The Night is Young_ I only was able to scratch the surface of what is possible but I liked the combination of mirror effects and distortion done in kdenlive along with the reactive GAN output. At a certain point it doesn't make sense to get the code to do something you can do faster manually, especially when the goal is a finished piece and not a "basic research" style investigation of the technology or tool building.

This piece required the most amount of exploration and curation of the machine learning tools. While _Robbie's Hobbies_ required a lot of experimentation, most of them were obvious failures, in this case the results were far more subjective and sensitive to tuning of parameters. The artist as curator I think is going to be a primary art form as machine learning tools develop, where much of the labour, as in collage, will be observation and exploration of the output from the machine; finding what is subjectively interesting and exciting to the artist and then organizing it in relation to the other generated art. For example, each animal texture looked better to me by adjusting the size and orientation of the texture and the strength of the mix between the texture and the original image. Then I coordinated, with only partial control, the timing of the animal sequences to create a relationship between them and/or the music. The design of the generator meant that I could only control the textural "destinations", but the "path" between them may actually be through other identifiable textures. An interesting concept on many levels - if you're a tiger, do you go through cheetah to get to octopus? The "map" of textures is created as the GAN learns, and [recent research](https://arxiv.org/pdf/2107.11186.pdf) shows that it is more organized than we expected.

I ended up taking the videos of Sarah at the recording session, so I saw her playing up close. Her enormous talent was obvious, but what stuck with me was her ability and need to feel the music, to not just know what to play but to embody it. Hot Bod’s concept and theme reflects the way she plays and thinks about music, and that let me show you the soul of the music through her playing, not just in this piece but all of them. Thanks Sarah!


## Source:

* [Videos, images and kdenlive project archive](https://spideroak.com/browse/share/SafeShare/Sound_Escapes_video_source)
  * Note: because of a [bug in kdenlive](https://bugs.kde.org/show_bug.cgi?id=439194) (as of v21.04.3) timeline clips of musicians (with greenscreens) may need to be disabled and re-enabled before they display correctly
* `source/code/`
  * Bash scripts for generating animal textured musicians with Optex
  * A very ugly version of the maua-stylegan2 script used for audio-reactivity. This is unusable as is, and requires the separated audio, which is not under an open licence, but gives an example of what was used. I adjusted and played with parameters and settings for each clip.
* [Custom models](https://spideroak.com/browse/share/SafeShare/Sound_Escapes_video_source/archives/models/hot_bod)


## Notes:

The basic pipeline to create the texture effect for each musician:

1. Extract frames from videos of the musician using [vid2frame](https://github.com/RKelln/vid2frame) with a strong rejection rate for similar frames to get around 100 different images of the musician.
2. Use Optex to apply textures to each of these frames for each texture (approximately 4 textures per animal type).
3. Use all of those images as training data for SWAGAN. For example:
```bash
$ python prepare_data.py ../datasets/animal_bass/ --out ../datasets/animal_bass_512x512.lmdb --resize distort --size 512

$ python train.py --project animal_bass --size 512 --arch swagan --augment --batch 12 --n_sample 8 --save_every 2000 --wandb ../datasets/animal_bass_512x512.lmdb
```
4. Select latents from the SWAGAN models. (Essentially selecting the textures I wanted to use in that section), for example:
```bash
$ python select_latents.py --ckpt ../rosinality-stylegan/checkpoint/animal_bass/120000.pt --arch swagan
```
5. Each section of the song edit the `maua_hot_bod.py` script to best match the desired audio-reactivity then run, for example, part of the bass solo:
```bash
$ python generate_audiovisual.py --ckpt ../rosinality-stylegan/checkpoint/animal_bass/120000.pt --audioreactive_file "audioreactive/examples/hot_bod.py" --duration 87 --offset 88 --out_size 896 --G_res 512 --arch swagan --batch 7 --audio_file data/audio/hot_bod.wav --latent_file workspace/animal_bass_120000_43_latents.npy --fps 30
```

## Footage:

  * Rhododendron flower photographs
    by [Andrew Drown](https://drown.photography)


## Code/Tools:

  * [kdenlive](https://kdenlive.org)
    Open source video editor

  * [ffmpeg](http://ffmpeg.org/)
    Open source audio and video tool

  * [StyleGAN 2 in PyTorch](https://github.com/rosinality/stylegan2-pytorch)
    by Kim Seonghyeon

  * [maua-stylegan2](https://github.com/JCBrouwer/maua-stylegan2)
    by Hans Brouwer

  * [Optex](https://github.com/JCBrouwer/OptimalTextures)
    by Hans Brouwer and Jim Kok
    * [Custom fork used in concert](https://github.com/RKelln/OptimalTextures/tree/video)

  * [https://github.com/RKelln/vid2frame](https://github.com/RKelln/vid2frame)

