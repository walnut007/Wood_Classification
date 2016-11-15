#coding:utf-8
"""
Author:walnut
Source:https://github.com/walnut007
"""

import os
from PIL import Image
import numpy as np

#read images

def load_data():
    data = np.empty((1600,100,100,3),dtype="float32")
	label = np.empty((1600,1),dtype="uint8")
    imgs = os.listdir("./wood")
    num = len(imgs)
    for i in range(num):
            img = Image.open("./wood/"+imgs[i])
            arr = np.asarray(img,dtype="float32")
            data[i,:,:,:] = arr
            label[i] = int(imgs[i].split('.')[0])
    data=np.transpose(data,(0,2,3,1))
    data=np.transpose(data,(0,2,1,3))
    return data, label








