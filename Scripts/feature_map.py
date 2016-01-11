#contains the id of the image in MSCOCO dataset relevant to the question
image_ids_train=open('../Data/Training/image_ids.txt','r').read().splitlines()
image_ids_val=open('../Data/Validation/image_ids.txt','r').read().splitlines()

# Coco folder contains the vgg_features.mat, which give the 4096 dimensional
# feature vector processed through VGG architecture. coco_vgg_IDmap.txt gives the mapping
# between coco images and feature vectors. 

maplist=open('../Data/Coco/coco_vgg_IDmap.txt','r').read().splitlines()
img_map={}
for ids in maplist:
	split=ids.split()
	img_map[split[0]]=split[1]
feature_ids_train=open("../Data/Training/feature_ids.txt",'w')
feature_ids_val=open("../Data/Validation/feature_ids.txt",'w')

for ids in image_ids_train:
	feature_ids_train.write(img_map[ids].encode('utf-8'))
	feature_ids_train.write('\n'.encode('utf-8'))
for ids in image_ids_val:
	feature_ids_val.write(img_map[ids].encode('utf-8'))
	feature_ids_val.write("\n".encode('utf-8'))