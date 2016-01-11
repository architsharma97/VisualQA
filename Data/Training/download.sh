#!/bin/bash
#Downloads the questions and annotations for training

wget http://visualqa.org/data/mscoco/vqa/Questions_Train_mscoco.zip
wget http://visualqa.org/data/mscoco/vqa/Annotations_Train_mscoco.zip

unzip \*.zip