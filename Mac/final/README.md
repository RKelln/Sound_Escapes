# i am a strange loop

Composer: **Mac Rogers** 

Visual FX Shader Artist: **Sol Sarratea**

Mac really dived into the concept and design, heavily inspired by Hofstadter's [I Am a Strange Loop](https://en.wikipedia.org/wiki/I_Am_a_Strange_Loop) book. I knew the perfect artist to help achieve this vision: [Sol Sarratea](https://solquemal.com/), a brilliant visual artist and huge fan of Hofstadter, who has the math and [shader](https://thebookofshaders.com/01/) skills to pull it off.

To better integrate the concert theme we explored the concept of people defining themselves by their favourite places in nature. Where Hofstadter explored how living emerges from inanimate matter, we wanted to loop back to how a self can define itself by its environment. Mac collected photos, text and audio recordings of friends’ and family's beloved places. This treasure trove then drove the visual concept.

Mac also integrated a story arc through the piece, a transition from inanimate, moving through self-replicating patterns, achieving life and/or/then digital life, and then transcending or deconstructing back to inanimate matter. Plus visually we all liked the idea of highlighting the Fibonacci sequence, fractals and other patterns found in nature. Like _Fade Into Black_ there were many themes, so the challenge was to manage the complexity, interactions and the transitions. To complicate matters, integrating the audio recordings required rearranging the piece thematically so that the voices could really shine.

Sol's research uncovered the [Droste effect](http://roy.red/posts/droste/), which had a Fibonacci-like feel but with beautiful curves and we were able to build on her [existing work](https://github.com/bu3nAmigue/bu3npattern/tree/video-texture) with [self-organizing textures](https://distill.pub/selforg/2021/textures/). Using textures derived from the photos Mac supplied in both effects I was able to start gluing the nature, nature-defining-self, and self-replicating pattern themes together.

To pair with the descriptions of favourite places I used [aphantasia](https://github.com/eps696/aphantasia) to dream up visuals based on the text. It turned out that the text actually required some translation to help guide the dreaming. This [art of ML text interface](https://ml.berkeley.edu/blog/posts/clip-art/) is well described by Charlie Snell - it is a new and intriguing way to control machine generated art. Using machine learning to generate the images provides a nice way to re-emphasize the underlying theme of patterns defining the self and the importance of converting/translating patterns as a form of genesis. People's brains dream of/remember their favourite places (now just a pattern of neural firing), translated to symbols by their brain, translated by me into other symbols that mean something similar but are better interpreted by a machine, which translates those symbols into visuals - based on the training it has received from a collection of text and image associations from the internet (i.e. how others have made associations between the symbols and images).

As Snell discusses, this feels like a conversation or collaboration with an alien mind; a gestalt mind, and in some ways, an ancient mind. The techniques for machine learning are still in their infancy so in some sense they mirror the early evolution of vision and symbolic processing. The low hanging fruit (at least for digital minds) of information processing will likely be the first "discovered" both by researchers and evolutionary processes.

It is this connection to, and greater understanding of, the fundamental information processing inherent in our universe that excites me about machine learning. This piece tries to represent a bit of that thrill.

Everything is tied together by the music – itself a translation to symbols by Mac, interpreted by the musicians, converted to air pressure pulses by their instruments, recorded digitally, and then translated again into visuals to match the rhythms and feel of the music. This long path of translation, encoding and decoding, has correspondence to the processing done in the machine learning algorithms (and in all intelligence). It is in the loss and regeneration of information that the magic happens. More poetically, sharing with each other leaves the imprint of your soul on one another and the things you create.

I had taken around 100 videos of local landscapes, and now I had an opportunity to use some of our footage to represent the inanimate and the beginning and ending of life. A bit of magic that we discovered at Ashbridge's Bay early one fall morning and a trip to High Park on Boxing Day with close friends. Visual magic then made to dance, making my own neurons dance each time the motion in the video felt intrinsically tied to the music. I spent a few months researching techniques to create a machine learning approach to generate this effect but in the end I had to do it manually. (If anyone wants to continue to pursue an ML approach please contact me!) 

The beginning and ending sections showcase this footage and technique and have 3 overlapping layers each representing one of the musicians. Here I am trying to create a cohesive whole, more than a single scene visually, trying to find a path between stillness and chaos, where life emerges and souls combine.

In the end this piece speaks to me because, like _Robbies Hobbies_, it too is a love letter to both people and places. Thanks to Mac and Sol for their genuine love for this piece and thoughtful, diligent effort bringing it alive.

## Source:

  * [Videos, images and kdenlive project archive](https://spideroak.com/browse/share/SafeShare/Sound_Escapes_video_source)
    * Note: because of a [bug in kdenlive](https://bugs.kde.org/show_bug.cgi?id=439194) (as of v21.04.3) timeline clips of musicians (with greenscreens) may need to be disabled and re-enabled before they display correctly
  * `source/code`
    * [TODO] Shader code for Fibonacci and Droste sequences 
  * `source/models/bu3npattern`
    * JSON model files created from [Texture Generation with Neural Cellular Automata](https://colab.research.google.com/drive/1KMlVFi2zXhE0_PHCBXC07oblcJf9E13s)
    * There is something broken/wrong with the format, such that multiple models are included in some files, but I couldn't manually concatenate models. Never figured out what is going on there.

## Notes:

The story used with aphantasia was a modified text based on the spoken text, in hopes of encouraging better images:

```
a quiet spot along a river bank with tall grass
a photo of Bolton, Ontario
tall grass folding over on itself 
a river edge lined with goldenrod, milkweed and Queen Anne’s lace
a closeup photo of milkweed by a river
a secret safe, tucked away by a river
monarch butterflies dancing in the milkweed
a girl transforming into a woman exploring independence, infatuation and self-awareness
aerial photo of vancouver island
a man walking in a forest with silent understandings
a happy contemplative person covered in mud in a forest
georgian bay water 
children playing on the beach with their grandparents in the 1970s
childrens toys on the beach
a child being hugged on the beach
sunrise reflecting on a still quiet lake 
a quiet misty lake with a loon in the water
closeup of a loon in a misty lake
a person running with the Seven Sisters mountain peaks in the background
a man running on the seven sisters hiking trail passing by a large white rock 
a indigenous witch woman turned to stone
seven upright and just women of the Tsimshian tribe turn into mountain peaks
seven indigenous women who look like trees
a pair of feet standing on beach sand 
a closeup of feet on the beach with a wave almost touching them
a person on a beach looking at the waves
a closeup of the a womans face with wind blowing her hair as she stands on a beach
a woman on a balcony of a house on the beach
the sun shining on an old woman standing on the beach
```

Run with these settings:
```bash
python illustra.py -i stories.txt --size 1200-1200 --length 76 --notext 0.3 -e 0.2 --decay 1.4 --colors 1.2 --contrast 0.9 --sharp 0.3 --fps 30 --fstep 10 
```
I found the videos generated automatically to be too low quality, but could build my own using:
```bash
ffmpeg -i _out/stories/_final/%05d.jpg -crf 22 -r 25 -preset veryslow _out/stories/stories.mp4
```

## Footage:

  * [Cell through Microscope Free Footage Clip](https://www.youtube.com/watch?v=_Rww1olT3HA)
    by Stock Heaven

  * Silver Lining, Uplifting Clouds, Epic Clouds, Sunset Waves close-up
    by [Beachfront B-roll](http://www.beachfrontbroll.com/)

  * [Conways_game_of_life_breeder_animation.gif](https://en.wikipedia.org/wiki/File:Conways_game_of_life_breeder_animation.gif)
    by George on Wikipedia

  * [Internet Map 2005]((https://en.wikipedia.org/wiki/File:Internet_map_1024.jpg))
    by Matt Britt on Wikipedia

  * [Raindrops in Super Slow Motion](https://www.youtube.com/watch?v=CMvaMD3j6o4)
    by Alizer AKDENİZ

  * [physarum network_2.gif](https://sagejenson.com/physarum)
    by Sage Jenson

  * Various photos from friends and family of Mac Rogers

  * Other footage by Ryan Kelln and Laura Soch

## Code/Tools:

  * [kdenlive](https://kdenlive.org)
    Open source video editor

  * [ffmpeg](http://ffmpeg.org/)
    Open source audio and video tool

  * [Texture Generation with Neural Cellular Automata](https://colab.research.google.com/drive/1KMlVFi2zXhE0_PHCBXC07oblcJf9E13s)
    Copyright 2021 Google LLC

  * [bu3nPattern](https://github.com/bu3nAmigue/bu3npattern/tree/video-texture)
    by Sol Sarratea

  * [Self-Organising Textures](https://distill.pub/selforg/2021/textures/)
    Neural Cellular Automata Model of Pattern Formation
    by Eyvind Niklasson, Alexander Mordvintsev, Ettore Randazzo, and Michael Levin

  * [Aphantasia](https://github.com/eps696/aphantasia)
    by vadim epstein

  * [Droste effect](http://roy.red/posts/droste/)
    by Roy Wiggins
