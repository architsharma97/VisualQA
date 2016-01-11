#!/bin/bash

#This script downloads and gets all the data preprocessed
#Read the guide for more information

#All Required Data is downloaded
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
#Uncomment the next line if you want to simultaneously train the model
#still untested for results, so evaluation script is not available

#python model_train.py
