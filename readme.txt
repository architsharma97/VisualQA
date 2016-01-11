***THE CODE IS STILL UNDER TESTING, SO THERE MAYBE BUGS***
***ANY HELP IS APPRECIATED***

This repository contains a script to train a model for visual question answering. The model contains a (to-be trained LSTM) and feature extraction from pre-trained VGG architecture. The model is heavy and will take a lot of time to train. So, train at your own risk. You are free to experiment with hyperparameters in the LSTM and MLP layers. Report back the results, if possible :)

Summary:
I have made a few scripts to download all the required data. On a fast internet connection, that should not take a lot of time. The only moderately heavy file is VGG Features for mscoco dataset.

All the python scripts are in 'Scripts' folder.
TODO: Comment on python scripts

For executing, first cd your way to the 'Visual-QA Directory'

Run these commands :
chmod +x ./run_this.sh
./run_this.sh