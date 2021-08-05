#!/bin/bash

# Create "dancing" painting animations using ConSinGAN:
# https://github.com/tohinz/ConSinGAN
# Used in the Sound Escapes concert:
# http://www.ryankelln.com/project/sound-escapes/

# animate
SCRIPT="python evaluate_model.py"
OPTIONS="--gpu 0 --anim_num_frames 300 --anim_frame_rate 15"

declare -a Paintings=("river_church"  
 "fall_sparkles"
# "winter_homestead"
 "summer_trees"
 "stream"
# "snowy_fallen_tree"
# "seaman"
 "rowboats"
 "rocky_hill"
# "reflections"
# "garage"
 "fishing_boats"
# "fall_shadows"
 "fall_fence"
 "fall_clouds")

for painting in ${Paintings[*]}; do
    echo $painting
    TRAINING_DIR=$(ls -td TrainedModels/$painting/*/ | head -1)
    echo "$TRAINING_DIR"
    $SCRIPT $OPTIONS --anim_beta 0.85 --anim_scale 0 --model_dir $TRAINING_DIR
    $SCRIPT $OPTIONS --anim_beta 0.95 --anim_scale 0 --model_dir $TRAINING_DIR
    ffmpeg -i $TRAINING_DIR/Evaluation/start_scale=1_alpha=0.1_beta=0.6_fps=15.mp4 \
    -framerate 15 -vf "minterpolate=fps=30:mi_mode=mci:me_mode=bidir,setpts=2*PTS" ${painting}_dance_0-85.mp4
    ffmpeg -i $TRAINING_DIR/Evaluation/start_scale=1_alpha=0.1_beta=0.5_fps=15.mp4 \
    -framerate 15 -vf "minterpolate=fps=30:mi_mode=mci:me_mode=bidir,setpts=2*PTS" ${painting}_dance_0-95.mp4
done


# Manual example:
# python evaluate_model.py --gpu 0 --model_dir TrainedModels/river_church/2021_05_05_23_50_23_animation_train_depth_3_lr_scale_0.1_act_lrelu_0.05 --beta 0.95 --anim_scale 1 --anim_num_frames 240 --anim_frame_rate 30
# ffmpeg -i TrainedModels/river_church/2021_05_05_23_50_23_animation_train_depth_3_lr_scale_0.1_act_lrelu_0.05/Evaluation/start_scale\=1_alpha\=0.1_beta\=0.95_fps\=15.mp4 -framerate 15 -vf "minterpolate=fps=30:mi_mode=mci:me_mode=bidir,setpts=2*PTS" river_church1mp4_30fps.mp4
