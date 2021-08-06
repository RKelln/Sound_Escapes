# Fade To Black

Composer: **Dhaivat Jani**

This piece went through a bunch of changes during its conceptualization, but had the fewest changes in implementation. Dhaivat was originally inspired by the beautiful tree outside his window and its transformation throughout the year. We had a good time biking around his neighbourhood looking for magnolia trees (which also had inspired him and we thought would make a good representation of the spring season).

The piece took a dramatic turn while it was being composed, and became more centered around our feelings regarding the climate emergency and how technology has shaped the world. So, we combined everything together.  I felt that despite a sort of overwhelming visual and thematic complexity, that complexity and layering represented our feelings when thinking about the combination of problems facing humanity.

The (many) layers in this piece are:

1. A history of human technology, as dreamt by a machine. Using the [aphantasia](https://github.com/RKelln/aphantasia) project, I fed it a list of 146 technologies from a few thousand years ago to today, basing it from the research done for the Creo Animam project. These images form an almost invisible backbone to the piece.
{{% youtube ZMKdpEwmQFE %}}
2. A sequence of videos representing humanity and our relationship with the environment and human industry. Pieced together from public domain and creative commons videos, I was particularly delighted by the [Prelinger Archives at the Internet Archive](https://archive.org/details/prelinger), and some government sources.
{{% youtube 3huPTrTJ2Zc %}}
3. The seasons of spring, fall and winter as imagined by [StyleGAN2](https://github.com/rosinality/stylegan2-pytorch). Using images based on seasonal search terms for training data these models were deliberately under-trained with far too little training data to create a vague sense of seasonal time - an impression of color and abstract form. These models were then animated using the [maua-stylegan2](https://github.com/JCBrouwer/maua-stylegan2) porject to react to the audio of the piece.
4. The tree and musicians: a filter or lens which, in this case, literally provides a glimpse of layer 2, the relationship between humanity, industry and nature.

I wanted to illustrate two relationships: those that see a landscape and think, "it's so beautiful and untouched" and those that think, "it's so empty and useless". Both consider the lack of human intervention a great resource or opportunity, but for very different reasons. I'd like to believe there is a perspective of mutuality that dissolves the separation of humanity from their environment.

This piece purposely feels unnerving to me, building to a sense of overwhelming terror or madness, but the final sequence fills me with renewed hope. Václav Havel said, "Hope is not the conviction that something will turn out well but the certainty that something makes sense, regardless of how it turns out". Fighting for justice and peace for all, including the non-human, will always make sense to me.

Dhaivat really made this piece personal, writing it amidst adversity, and I did my best to respect and honor that, so I was grateful when he thought I had captured the feelings well. For me it was an attempt to bottle the feeling of being changed, with the final afterimage echoing the initial inspiration for this piece and a reaffirmed love of nature, including us.


## Source:

  * [Videos, images and kdenlive project archive](https://spideroak.com/browse/share/SafeShare/Sound_Escapes_video_source)
    * Note: because of a [bug in kdenlive](https://bugs.kde.org/show_bug.cgi?id=439194) (as of v21.04.3) timeline clips of musicians (with greenscreens) may need to be disabled and re-enabled before they display correctly
  * [Models for seasons](https://spideroak.com/browse/share/SafeShare/Sound_Escapes_video_source/archives/models/fade_to_black)


## Notes:

Much of the kdenlive project has been "pre-rendered" into more easily to work with sequences, since the render times and complications from bugs was really slowing down the edit.

Each season was trained using [StyleGAN 2 in PyTorch](https://github.com/rosinality/stylegan2-pytorch), for exmaple:
```bash
python prepare_data.py ../datasets/spring/ --out ../datasets/spring.lmdb --size 512

python train.py --project spring --size 512 --arch swagan --augment --batch 12 --n_sample 8 --save_every 2000 --wandb ../datasets/spring.lmdb
```

Then that model was animated using [maua-stylegan2](https://github.com/JCBrouwer/maua-stylegan2), for example:

```bash
python select_latents.py --ckpt ../rosinality-stylegan/checkpoint/spring/020000.pt --res 512 --arch swagan

python generate_audiovisual.py --ckpt ../rosinality-stylegan/checkpoint/spring/020000.pt --audioreactive_file "audioreactive/examples/fade_to_black.py" --duration 77 --out_size 512 --G_res 512 --arch swagan --batch 7 --audio_file data/audio/fade_to_black.wav --latent_file workspace/spring_020000_fade_to_black_latents.npy --fps 30
```

## Footage:

  * [Pollution Crime](https://www.youtube.com/watch?v=rIBEn5WsugE)
    by INTERPOL

  * [Air Pollution HD Stock Video](https://www.youtube.com/watch?v=lq4ivmk9llM)
    by CHANNEL PMI - FREE STOCK VIDEO

  * [Water Pollution HD Stock Video](https://www.youtube.com/watch?v=T8wQ6y_AQGE)
    by CHANNEL PMI - FREE STOCK VIDEO

  * [Protest HD Stock Video](https://www.youtube.com/watch?v=JiaMhAWHkzg)
    by CHANNEL PMI - FREE STOCK VIDEO

  * [Fire Behaviour: Observation & Training](https://www.youtube.com/watch?v=p1iZPR6aIBc)
    by CFA (Country Fire Authority)

  * [Survival Under Atomic Attack](https://archive.org/details/Survival1951)
    by U.S. Office of Civil Defense 

  * [Wheels of Progress](https://archive.org/details/Wheelsof1950)
    by Zenith Cinema Services, Inc. 

  * [Black Lives Matters - George Floyd protests videos](https://www.youtube.com/watch?v=d4HKXLks-VA)
    by Ram Biole

  * [PROTEST: Youth Global Warming Strike, London 2019](https://www.youtube.com/watch?v=h8o_YP0YKLc)
    by Londisland

  * [Full Earth Video - April 1st 2018](https://www.youtube.com/watch?v=UZOOL3kYU9k)
    by Blueturn Earth

  * [Frogger Highway](http://www.beachfrontbroll.com/2012/01/1-clip-needs-frog.html)
    by Beachfront B-Roll

  * [Newyork Night View Free Footage Clip](https://www.youtube.com/watch?v=3iasQGbmGYg)
    by Stock Heaven

  * [Rare Footage of 9/11 WTC Attack Military videos](https://www.youtube.com/watch?v=rHPZ0ue2chQ)
    by U.S. Military Cache
  
  * Other footage by Ryan Kelln and Laura Soch

## Code/Tools:

  * [kdenlive](https://kdenlive.org)
    Open source video editor

  * [ffmpeg](http://ffmpeg.org/)
    Open source audio and video tool

  * [StyleGAN 2 in PyTorch](https://github.com/rosinality/stylegan2-pytorch)
    by Kim Seonghyeon

  * [Aphantasia](https://github.com/eps696/aphantasia)
    by vadim epstein
    * [Custom fork used in concert](https://github.com/RKelln/aphantasia) by Ryan Kelln

  * [maua-stylegan2](https://github.com/JCBrouwer/maua-stylegan2)
    by Hans Brouwer

  * [https://github.com/RKelln/pyimgdata](https://github.com/RKelln/pyimgdata)