#!/bin/bash
#downloads the questions and annotations for validation from visualqa.org

wget http://visualqa.org/data/mscoco/vqa/Questions_Val_mscoco.zip
wget http://visualqa.org/data/mscoco/vqa/Annotations_Val_mscoco.zip

unzip \*.zip