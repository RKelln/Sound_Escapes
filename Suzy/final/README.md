# Robbie's Hobbies

Composer: **Suzy Wilde**

This piece is dedicated to Robert Wilde, Suzy's grandfather, and features his landscape paintings and a cameo of him playing the piano for her as a child. This was really a delight to work on, as I'm thrilled any time I can be working on art that acts as a love letter to your friends, family or communities. It was also one of the more frustrating and challenging pieces (technically).

Supposedly machine learning is good at style transfer (copying the style of one image to the content of another), but my video results, with a set of less than 20 paintings as training data, weren’t what I was looking for. These techniques still struggle with consistent video results (often suffering from flicker or wildly different styleization each frame). I tried many different approaches, including a number of non-neural net image processing algorithms, but if the stylization was good then it was bad temporally, if the video was good then the stylization was weak. The end result was a mix of effects built into kdenlive and [ReReVST](https://github.com/RKelln/ReReVST-Code).

I also found a few projects that I thought would be perfect for animating landscape paintings, but had worse results than in the papers or were limited in resolution (or both). In the end it required a lot of video editing to integrate these techniques, but I was happy that I got to use them, likely for the first time, in an art context.

I'm looking forward to this video being updated when techniques improve and high resolution style-aware animation is possible. My ultimate vision is to make the paintings move realistically in the slower sections in the beginning and then dance in the uptempo sections with the musician footage looking like it was part of the painting.

It is always a pleasure working with Suzy, as she is such an emotive and lyrical artist, something I deeply appreciate but isn't how I create art on my own.


## Source:

* [Videos, images and kdenlive project archive](https://spideroak.com/browse/share/SafeShare/Sound_Escapes_video_source)
  * Note: because of a [bug in kdenlive](https://bugs.kde.org/show_bug.cgi?id=439194) (as of v21.04.3) timeline clips of musicians (with greenscreens) may need to be disabled and re-enabled before they display correctly
* `code/`
  * Bash scripts training and animation generation with ConSinGAN
  * Fragment shader (used with VEDA) for kaleidoscope effects
    * Note that shader parameters were tweaked for differnet sections
* [Models for ReReVST](https://spideroak.com/browse/share/SafeShare/Sound_Escapes_video_source)


## Notes:

Example of ReReVST training:

```bash
python train.py --cuda --gpu 0 --epoches 4 --batchSize 4 --lr 1e-4 \
--dynamic_filter --both_sty_con --relax_style \
--style_content_loss --recon_loss --tv_loss --temporal_loss \
--data_sigma --data_w --adaversarial_loss \
--content_data data/content/val2017 \
--style_data ../../datasets/paintings_5crop_unsharp \
--outf result/paintings2 \
--loadSize 512
```

Example of ReReVST inference:

```bash
python generate_real_video.py --no_global --style_scale 2 --content inputs/suzy_chris_end_1.mp4 --model Model/style_net-paintings-2.pth --style inputs/style_paintings/robbie/summer_trees.jpg --output suzy_chris_end_1
```


## Footage:

  * Paintings by Robert Wilde
    photographed by Suzy Wilde

  * [Canvas texture](https://unsplash.com/photos/xz485Eku8O4)
    by Annie Spratt on Unsplash

  * [Watercolor wash Kdenlive FX wipe](https://www.pling.com/p/1106266/)

  * [Painting Kdenlive FX wipe](https://www.pling.com/p/1568961/)
    by Ryan Kelln


## Code / Tools:

  * [kdenlive](https://kdenlive.org)
    Open source video editor

  * [ffmpeg](http://ffmpeg.org/)
    Open source audio and video tool

  * [Consistent Video Style Transfer via Relaxation and Regularization](https://github.com/daooshee/ReReVST-Code)]
    by Wenjing Wang, Shuai Yang, Jizheng Xu, and Jiaying Liu
    * [Code fork used in this concert](https://github.com/RKelln/ReReVST-Code) by Ryan Kelln

  * [ConSinGAN](https://github.com/tohinz/ConSinGAN)
    by Tobias Hinz

  * [Animating Landscape](https://github.com/endo-yuki-t/Animating-Landscape)
    by Yuki Endo and Yoshihiro Kanamori and Shigeru Kuriyama
    * [http://www.cgg.cs.tsukuba.ac.jp/~endo/projects/AnimatingLandscape/](http://www.cgg.cs.tsukuba.ac.jp/~endo/projects/AnimatingLandscape/)

  * [DeepLandscape: Adversarial Modeling of Landscape Videos](https://github.com/saic-mdal/deep-landscape)
    by E. Logacheva, R. Suvorov, O. Khomenko, A. Mashikhin, and V. Lempitsky
    * [https://saic-mdal.github.io/deep-landscape/](https://saic-mdal.github.io/deep-landscape/)

  * [pytorch-AdaIN](https://github.com/naoto0804/pytorch-AdaIN)
    by Naoto Inoue

  * [DeOldify](https://github.com/jantic/DeOldify.git)
    by Jason Antic

  * [timecraft](https://github.com/xamyzhao/timecraft)
    by Amy Zhao, Guha Balakrishnan, Kathleen M. Lewis, Fredo Durand, John Guttag, Adrian V. Dalca

  * [VEDA](https://veda.gl/):
    VJ / Livecoding with GLSL


## Sound Escapes

This piece is part of the [Sound Escapes concert](http://www.ryankelln.com/project/sound-escapes/) in collaboration with [Spectrum Music](https://www.spectrummusic.ca/).


## Licence

Robbie's Hobbies visuals and code is licensed under a
Creative Commons Attribution-ShareAlike 4.0 International License.

You should have received a copy of the license along with this
work. If not, see <http://creativecommons.org/licenses/by-sa/4.0/>.

Please note, the audio for Robbie's Hobbies and the composition are licenced separately, copyright Spectrum Music and Suzy Wilde, repsectively.