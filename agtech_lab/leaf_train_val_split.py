import os
import random
import shutil

#0.8 / 0.2로 train_val 나누기
path = "/home/hyeonji/YOLOv8/alarad_P2_V1_300/images"

#파일목록 읽어오기
file_list =[]
picked_file60=[]

for root, subdirs, files in os.walk(path):
    for i in files:
        file_list.append(i)

print("len file list:",len(file_list))
#랜덤으로 20% 뽑기
picks = random.sample(range(0,299),60) #300의 0.2 => 60
print(picks)
for idx in picks:
    fname = file_list[idx].split('.')[0]
    picked_file60.append(fname)
    print(fname)

#20%를 val로 move
#image
for fname in picked_file60:
    shutil.move('/home/hyeonji/YOLOv8/alarad_P2_V1_300/images/'+fname+'.png','/home/hyeonji/YOLOv8/alarad_P2_V1_300/images/val/'+fname+'.png')

#label
for fname in picked_file60:
    shutil.move('/home/hyeonji/YOLOv8/alarad_P2_V1_300/labels/'+fname+'.txt','/home/hyeonji/YOLOv8/alarad_P2_V1_300/labels/val/'+fname+'.txt')

#나머지 80%는 train에 저장
