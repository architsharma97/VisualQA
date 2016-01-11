#!/bin/bash
#Downloads the VGG Features on Dataset

wget http://cs.stanford.edu/people/karpathy/deepimagesent/coco.zip
unzip coco.zip -d .
cp ./coco/vgg_feats.mat .
rm -rf ./coco/vgg_feats.mat