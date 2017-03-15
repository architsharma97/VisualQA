#!/bin/bash
# downloads the VGG features on ms coco dataset

wget http://cs.stanford.edu/people/karpathy/deepimagesent/coco.zip
unzip coco.zip -d .
cp ./coco/vgg_feats.mat .
rm -rf ./coco/vgg_feats.mat