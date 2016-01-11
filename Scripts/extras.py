import operator
import numpy as np
import scipy.io

def frequentAnswers(questions_train, answers_train, features_ids, questions_length, maxAnswers):
	answer_count={}
	for answer in answers_train:
		if answer in answer_count:
			answer_count[answer]+=1
		else:
			answer_count[answer]=1
	sorted_answers=sorted(answer_count.items(),key=operator.itemgetter(1),reverse=True)[0:maxAnswers]
	top_answers=[]
	for answer in sorted_answers:
		top_answers.append(answer[0])
	#new set of top answers
	new_answers_train,new_questions_train,new_features_id, new_questions_length=[],[],[],[]

	for i in range(len(answers_train)):
		if answers_train[i] in top_answers:
			new_features_id.append(features_ids[i])
			new_questions_train.append(questions_train[i])
			new_answers_train.append(answers_train[i])
			new_questions_length.append(questions_length[i])

	return (new_questions_train,new_answers_train,new_features_id,new_questions_length)

def questions_tensor(questions, nlp, max_len):
	nb_examples = len(questions)
	word2vec_dim = nlp(questions[0])[0].vector.shape[0]
	questions_tensor=np.zeros((nb_examples, max_len, word2vec_dim))
	for i in range(nb_examples):
		tokens=nlp(questions[i])
		for j in range(len(tokens)):
			questions_tensor[i,j,:]=tokens[j].vector
	return questions_tensor

def image_matrix(features_id):
	#mat file 4096x123287, transpose allows feature detection directly
	VGGFeatures=np.transpose(scipy.io.loadmat('../Data/Coco/vgg_feats.mat')['feats'])
	nb_examples=len(features_id)
	image_matrix=np.zeros((nb_examples, VGGFeatures.shape[1]))
	for i in range(nb_examples):
		image_matrix[i,:]=VGGFeatures[features_id[i],:]
	return image_matrix

def answers_matrix(answers, le):
	nb_classes=le.classes_.shape[0]
	#assigns numerical classes according to pre-trained convention
	y=le.transform(answers)
	#for marking the class to which the answer belongs
	Y=np.zeros((len(y),nb_classes))
	for i in range(len(y)):
		Y[i,y[i]]=1.
	return Y