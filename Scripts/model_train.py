#hyperparameter tuning needs to be done
import scipy.io
import extras
import numpy as np

from sklearn import preprocessing
from sklearn.externals import joblib

from keras.models import Sequential
from keras.layers.core import Dense, Activation, Merge, Reshape, Dropout
from keras.layers.recurrent import LSTM

from spacy.en import English

questions_train_all=open('../Data/Training/question_train.txt','r').read().decode('utf-8').splitlines()
answers_train_all=open('../Data/Training/answers_train.txt','r').read().decode('utf-8').splitlines()
questions_length_train_all=open('../Data/Training/questions_length.txt','r').read().splitlines()
feature_ids_train_all=open('../Data/Training/feature_ids.txt','r').read().splitlines()

#select frequent 1000 answers and corresponding questions sequentially
# questions_train, answers_train, feature_ids_train, questions_length_train=extras.frequentAnswers(questions_train_all, answers_train_all, feature_ids_train_all, questions_length_train_all, 1000)

#test the imported 
# unique=[]
# for answer in answers_train:
# 	if answer not in unique:
# 		unique.append(answer)

questions_val_all=open('../Data/Validation/question_val.txt','r').read().decode('utf-8').splitlines()
answers_val_all=open('../Data/Validation/answers_val.txt','r').read().decode('utf-8').splitlines()
questions_length_val_all=open('../Data/Validation/questions_length.txt','r').read().splitlines()
feature_ids_val_all=open('../Data/Validation/feature_ids.txt','r').read().splitlines()

#select 1000 most frequent answers in validation
# questions_val, answers_val, feature_ids_val, questions_length_val=extras.frequentAnswers(questions_val_all, answers_val_all, feature_ids_val_all, questions_length_val_all, 1000)

#for final training
questions=questions_train_all+questions_val_all
answers=answers_train_all+answers_val_all
feature_ids=feature_ids_train_all+feature_ids_val_all
questions_length=questions_length_train_all+questions_length_val_all

questions, answers, feature_ids, questions_length=extras.frequentAnswers(questions, answers, feature_ids, questions_length, 1000)
questions_length=[int(ql) for ql in questions_length]
features_ids=[int(f) for f in feature_ids]

#convert the answers
le=preprocessing.LabelEncoder()
le.fit(answers)
#encoder will be required during evaluation 
joblib.dump(le,'../Models/labelencoder.pkl')

#constants for the rest of the code
img_dim=4096
#maximum length of a question in the training and validation set
max_len=np.amax(np.asarray(questions_length))+1
#standard word2vec length
word2vec_dim=300
ans_classes=len(list(le.classes_))

#image features are already precomputed on the training set
image_model=Sequential()
image_model.add(Reshape(input_shape=(img_dim,), dims=(img_dim,)))

#LSTM model with one hidden layer
language_model=Sequential()
language_model.add(LSTM(output_dim=512, return_sequences=False,input_shape=(max_len, word2vec_dim)))

model=Sequential()
model.add(Merge([image_model, language_model],mode='concat',concat_axis=1))
for i in range(3):
	model.add(Dense(1024,init='uniform'))
	model.add(Activation('softmax'))
	model.add(Dropout(0.5))
model.add(Dense(ans_classes))
model.add(Activation('softmax'))

open('../Models/vqa_model.json','w').write(model.to_json())

model.compile(loss='categorical_crossentropy', optimizer='rmsprop')

print 'Loading word2vec...'
nlp=English()

print 'Converting data into trainable form...'

print 'Converting questions...'
q=extras.questions_tensor(questions,nlp, max_len)

print 'Getting image features'
img=extras.image_matrix(feature_ids)

print 'Converting answers'
ans=extras.answers_matrix(answers,le)

print 'Loaded\nTraining the model...'
model.fit([img, q],ans, nb_epoch=1, batch_size=1024)

model.save_weights("../Models/weights.hdf5")
