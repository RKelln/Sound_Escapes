#!/bin/bash

# training

OPTIONS="--gpu 0 --train_mode animation --train_stages 7 --max_size -1 --height 1080"

python main_train.py $OPTIONS --input_name Images/Animation/river_church.jpg

python main_train.py $OPTIONS --input_name Images/Animation/fall_sparkles.jpg

python main_train.py $OPTIONS --input_name Images/Animation/winter_homestead.jpg

python main_train.py $OPTIONS --input_name Images/Animation/summer_trees.jpg

python main_train.py $OPTIONS --input_name Images/Animation/stream.jpg

python main_train.py $OPTIONS --input_name Images/Animation/snowy_fallen_tree.jpg

python main_train.py $OPTIONS --input_name Images/Animation/seaman.jpg

python main_train.py $OPTIONS --input_name Images/Animation/rowboats.jpg

python main_train.py $OPTIONS --input_name Images/Animation/rocky_hill.jpg

python main_train.py $OPTIONS --input_name Images/Animation/reflections.jpg

python main_train.py $OPTIONS --input_name Images/Animation/garage.jpg

python main_train.py $OPTIONS --input_name Images/Animation/fishing_boats.jpg

python main_train.py $OPTIONS --input_name Images/Animation/fall_shadows.jpg

python main_train.py $OPTIONS --input_name Images/Animation/fall_fence.jpg

python main_train.py $OPTIONS --input_name Images/Animation/fall_clouds.jpg



#python main_train.py --gpu 0 --train_mode animation --train_stages 7 --max_size -1 --height 1080 --input_name Images/Animation/reflections.jpg