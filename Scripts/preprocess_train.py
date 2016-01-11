import sys
import json
import nltk
import progressbar

def most_frequent(answers):
	list={}
	for i in range(10):
		list[answers[i]['answer']]=1
	max_frequency=1
	ans=answers[0]['answer']
	for i in range(10):
		list[answers[i]['answer']]+=1
		if list[answers[i]['answer']]>max_frequency:
			max_frequency=list[answers[i]['answer']]
			ans=answers[i]['answer']
	return str(ans.replace(u'\u2018',"'").replace(u'\u2019',"'"))

quesFile_train='../Data/Training/OpenEnded_mscoco_train2014_questions.json'
annFile_train='../Data/Training/mscoco_train2014_annotations.json'
questions_file=open('../Data/Training/question_train.txt','w')
questions_length_file=open('../Data/Training/questions_length.txt','w')
answers_file=open('../Data/Training/answers_train.txt','w')
coco_id=open('../Data/Training/image_ids.txt','w')

questions=json.load(open(quesFile_train,'r'))['questions']
answers=json.load(open(annFile_train,'r'))['annotations']

#most frequent answer is chosen from the answer list
pbar=progressbar.ProgressBar()
for i in pbar(range(len(questions))):
	q=questions[i]
	a=answers[i]
	questions_file.write(q['question'].encode('utf-8'))
	questions_file.write("\n".encode('utf-8'))
	
	questions_length_file.write(str(len(nltk.word_tokenize(q['question']))).encode('utf-8'))
	questions_length_file.write("\n".encode('utf-8'))

	coco_id.write(str(q['image_id']).encode('utf-8'))
	coco_id.write('\n'.encode('utf-8'))

	answers_file.write(str(most_frequent(a['answers'])).encode('utf-8'))
	answers_file.write('\n'.encode('utf-8'))