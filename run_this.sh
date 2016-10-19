#!/bin/bash

#script downloads and preprocesses all the data
#read the guide for more information

#download all required data
cd ./Data/Coco
chmod +x ./download.sh
./download.sh

cd ../Training
chmod +x ./download.sh
./download.sh

cd ../Validation
chmod +x ./download.sh
./download.sh

cd ../../Scripts
python preprocess_train.py
python preprocess_val.py

#Optional
#uncomment the next line if you want to simultaneously train the model
#still untested for results, so evaluation script is not available

#python model_train.py
