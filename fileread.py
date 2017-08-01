import os
from os import listdir, getcwd
from os.path import join
import  numpy as np
thresh = 0.24
valpath = 'E:/valdata/vallabels/'
finalpath = 'E:/valdata/alllabels.txt'
all_obj=open(finalpath,'w')
val_list = os.listdir(valpath)
for val_obj in val_list:
    val_path = os.path.join(valpath,val_obj)
    text=open(val_path,'r').read().strip().split()
    for x in range(len(text)):
        all_obj.write(text[x]+' ')
    all_obj.write('\n')
all_obj.close()








