# Bird Brained

Composer: **Jackson Welchner**

Jackson's pieces often have a cheekiness to them and challenge the musicians and leave them whooping in delight once it grooves. Bird Brained piece fits the mould and is themed visually around bird flocking.

At the outset I knew I wanted to get a [Craig Reynold's inspired](https://www.red3d.com/cwr/boids/) 'boid' simulation going, but wasn't sure how to tie that to the music. Fortunately for me [Stephen Young](https://github.com/kyrick/godot-boids-acceleration-structure) had already done some experiments with boids using my favourite game engine: [Godot](https://godotengine.org/). From there I experimented with making the simulation look even better from the perspective of a bird watcher and added an interface that allowed someone to "play" the bird flock in time to music. The final controls scheme allowed for adding and removing boids, changing their speed, all of the parameters controlling flocking behaviour, some special effects and perhaps most beautifully a painting mode where you could use the keyboard or a midi keyboard to colorize the boids based on the note pressed and they would paint the screen with their color, creating a sort of cloud of color reminiscent of fireworks or slow motion [Holi festival](https://en.wikipedia.org/wiki/Holi) colored powder.

You can try this for yourself by [downloading my software](https://github.com/RKelln/godot-boids-acceleration-structure/releases).

A lot of the piece didn't fit musically with bird flocking however, so I had to get creative and started to draw on a lot of inspiration, mainly from [The Books](https://www.youtube.com/watch?v=WnzZimagUjM), whose handcrafted music videos first inspired me to want to make video to music. Laura and I searched for additional Creative Commons footage and discovered a few pieces of gold too: [Caleb Wood's bird shit](https://vimeo.com/58970291) and some fantastic footage of ducks being ducky.

To really explore the bird theme I used the [Big Sleep](https://github.com/lucidrains/big-sleep) project to imagine life from a bird's point of view and even a world where the composer, musicians and I were all birds.

Some of the sections of this piece I really struggled with, but everything came together in the end. For example, Laura and I spent most of a day learning how to play the bird sim together - her on mouse and me on keyboards, trying to match the birds to the piano solo. Despite the frustrations of software bugs and learning a new instrument, it was a great experience to be (the first?) flocking instrumentalists.

Building little art instruments like that really makes me happy, and Jackson always provides a great piece to jam to.


## Source:

  * [Videos, images and kdenlive project archive](https://spideroak.com/browse/share/SafeShare/Sound_Escapes_video_source)
    * Note: because of a [bug in kdenlive](https://bugs.kde.org/show_bug.cgi?id=439194) (as of v21.04.3) timeline clips of musicians (with greenscreens) may need to be disabled and re-enabled before they display correctly
  * [Boids code](https://github.com/RKelln/godot-boids-acceleration-structure/tree/jackson)
  * [Bird Brained boids download](https://github.com/RKelln/godot-boids-acceleration-structure/releases)
  

## Footage:

  * [Lake, sunset - birds flying to the camera - gopro (1080p)](https://www.youtube.com/watch?v=lhgGDBMz3II)
    by Free Footage For You - YouTube channel

  * [gull flying slow mo bird and sky](https://www.youtube.com/watch?v=dfA3UASzwS0)
    by galosstiftelsen

  * [Pigeon plumage](https://pixabay.com/videos/pigeons-bird-feather-plumage-39263/)
    by Roy Buri from Pixabay

  * [Mandarin duck - Mandarijneend - Aix galericulata](https://vimeo.com/49589113)
    by Watervogelbond

  * [Happy hopping Barnacle goose juvenile](https://www.youtube.com/watch?v=thEOf3tH8rI)
    by Vesa Leinonen

  * [Watervogelbond - Sylvan Heights Vogel Park](https://vimeo.com/79031925)
    by Watervogelbond

  * [bird shit](https://vimeo.com/58970291)
    by caleb wood 

  * [Meet the Locals: Ruru](https://www.youtube.com/watch?v=vZSda4jaBMY)
    by New Zealand Department of Conservation

  * [Adult Geese and Baby Geese Crossing the Street (Shot w/Nikon Coolpix P1000)](https://www.youtube.com/watch?v=1YhsooDk3sk)
    by WildLife Videography

  * [Bird Flying - Free Stock Creative Commons Video](https://www.youtube.com/watch?v=FrRXDYUatf4)
    by Freestocks

  * [Birds On The Post](http://www.beachfrontbroll.com/2011/09/something-little-more-scenic.html)
    by Beachfront B-Roll

  * [Various Seagull footage](http://www.beachfrontbroll.com/2013/11/seagulls.html)
    by Beachfront B-Roll


## Code/Tools:

  * [kdenlive](https://kdenlive.org)
    Open source video editor

  * [ffmpeg](http://ffmpeg.org/)
    Open source audio and video tool

  * [Godot Engine](https://godotengine.org/)
    Free and open source 2D and 3D game engine

  * [Godot Midi player](https://bitbucket.org/arlez80/godot-midi-player)
    by きのもと 結衣 (Yui Kinomoto)

  * [Boids in Godot with Acceleration Structure](https://github.com/kyrick/godot-boids-acceleration-structure)
    by Stephen Young
    * [Bird Brained in Godot](https://github.com/RKelln/godot-boids-acceleration-structure/tree/jackson) by Ryan Kelln

  * [Big Sleep](https://github.com/lucidrains/big-sleep)
    by Phil Wang
    * [Big Sleep fork used in this project](https://github.com/RKelln/big-sleep)
      by Ryan Kelln

  * [Super Resolution API](https://deepai.org/machine-learning-model/torch-srgan)
    by DeepAI
