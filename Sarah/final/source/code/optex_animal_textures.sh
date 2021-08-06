#!/usr/bin/env bash

# NOTES: 
# As size increases, the content strnegth generally has to go down. 
# e.g. from 500 to 896, content stength went down approximately 0.02

OUTPUT="output/caleb_electric"
STYLE_BASEDIR="../datasets/animal_textures"
CONTENT="../content/caleb_electric"
ITERS=800
SIZE=896
SEED=1


python optex.py --style $STYLE_BASEDIR/anemone \
--content_strength 0.04 \
--style_scale 0.4 \
--content $CONTENT \
--iters $ITERS \
--size $SIZE \
--seed $SEED \
--output $OUTPUT

python optex.py --style $STYLE_BASEDIR/bee \
--content_strength 0.02 \
--style_scale 0.65 \
--content $CONTENT \
--iters $ITERS \
--size $SIZE \
--seed $SEED \
--output $OUTPUT

python optex.py --style $STYLE_BASEDIR/blue_ringed_octopus \
--content_strength 0.03 \
--style_scale 0.75 \
--content $CONTENT \
--iters $ITERS \
--size $SIZE \
--seed $SEED \
--output $OUTPUT

python optex.py --style $STYLE_BASEDIR/cheetah \
--content_strength 0.06 \
--style_scale 0.5 \
--content $CONTENT \
--iters $ITERS \
--size $SIZE \
--seed $SEED \
--output $OUTPUT

python optex.py --style $STYLE_BASEDIR/cheetah2 \
--content_strength 0.07 \
--style_scale 0.65 \
--content $CONTENT \
--iters $ITERS \
--size $SIZE \
--seed $SEED \
--output $OUTPUT

python optex.py --style $STYLE_BASEDIR/clown \
--content_strength 0.05 \
--style_scale 0.3 \
--content $CONTENT \
--iters $ITERS \
--size $SIZE \
--seed $SEED \
--output $OUTPUT

python optex.py --style $STYLE_BASEDIR/clown2 \
--content_strength 0.05 \
--style_scale 1.2 \
--content $CONTENT \
--iters $ITERS \
--size $SIZE \
--seed $SEED \
--output $OUTPUT

python optex.py --style $STYLE_BASEDIR/eagle \
--content_strength 0.04 \
--style_scale 0.3 \
--content $CONTENT \
--iters $ITERS \
--size $SIZE \
--seed $SEED \
--output $OUTPUT

python optex.py --style $STYLE_BASEDIR/giraffe \
--content_strength 0.05 \
--style_scale 0.5 \
--content $CONTENT \
--iters $ITERS \
--size $SIZE \
--seed $SEED \
--output $OUTPUT

python optex.py --style $STYLE_BASEDIR/koy \
--content_strength 0.065 \
--style_scale 0.2 \
--content $CONTENT \
--iters $ITERS \
--size $SIZE \
--seed $SEED \
--output $OUTPUT

python optex.py --style $STYLE_BASEDIR/leopard \
--content_strength 0.07 \
--style_scale 0.5 \
--content $CONTENT \
--iters $ITERS \
--size $SIZE \
--seed $SEED \
--output $OUTPUT

python optex.py --style $STYLE_BASEDIR/monarch \
--content_strength 0.08 \
--style_scale 0.3 \
--content $CONTENT \
--iters $ITERS \
--size $SIZE \
--seed $SEED \
--output $OUTPUT

python optex.py --style $STYLE_BASEDIR/octopus \
--content_strength 0.05 \
--style_scale 0.45 \
--content $CONTENT \
--iters $ITERS \
--size $SIZE \
--seed $SEED \
--output $OUTPUT

python optex.py --style $STYLE_BASEDIR/parrot \
--content_strength 0.06 \
--style_scale 0.2 \
--content $CONTENT \
--iters $ITERS \
--size $SIZE \
--seed $SEED \
--output $OUTPUT

python optex.py --style $STYLE_BASEDIR/peacock \
--content_strength 0.07 \
--style_scale 0.3 \
--content $CONTENT \
--iters $ITERS \
--size $SIZE \
--seed $SEED \
--output $OUTPUT

python optex.py --style $STYLE_BASEDIR/peacock2 \
--content_strength 0.07 \
--style_scale 0.5 \
--content $CONTENT \
--iters $ITERS \
--size $SIZE \
--seed $SEED \
--output $OUTPUT

python optex.py --style $STYLE_BASEDIR/pheasant \
--content_strength 0.08 \
--style_scale 0.35 \
--content $CONTENT \
--iters $ITERS \
--size $SIZE \
--seed $SEED \
--output $OUTPUT

python optex.py --style $STYLE_BASEDIR/slug \
--content_strength 0.05 \
--style_scale 0.5 \
--content $CONTENT \
--iters $ITERS \
--size $SIZE \
--seed $SEED \
--output $OUTPUT

python optex.py --style $STYLE_BASEDIR/tiger \
--content_strength 0.06 \
--style_scale 0.6 \
--content $CONTENT \
--iters $ITERS \
--size $SIZE \
--seed $SEED \
--output $OUTPUT

python optex.py --style $STYLE_BASEDIR/zebra \
--content_strength 0.07 \
--style_scale 0.3 \
--content $CONTENT \
--iters $ITERS \
--size $SIZE \
--seed $SEED \
--output $OUTPUT

