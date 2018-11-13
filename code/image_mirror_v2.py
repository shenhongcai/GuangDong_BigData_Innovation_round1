import numpy as np
import os
from PIL import Image
import cv2
import copy
i=0
file_dir='.\\source\\'
dst='.\\result\\'

def  cv_imread(filePath):
     cv_img=cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)
     return cv_img

##水平镜像函数
def image_Lmirror(file_path): 
        image = cv_imread(file_path)
        height=image.shape[0]
        width=image.shape[1]
        h=height
        w=width
        size = (width,height)
        iUD = copy.deepcopy(image)
        iLR = copy.deepcopy(image)
        iAcross=copy.deepcopy(image)
        for i in range(height):
             for j in range(width):
                iLR[i,w-1-j] = image[i,j]   #水平镜像
        return iLR
##垂直镜像函数
def image_Vmirror(file_path):
        image = cv_imread(file_path)
        height=image.shape[0]
        width=image.shape[1]
        h=height
        w=width
        size = (width,height)
        iUD = copy.deepcopy(image)
        for i in range(height):
             for j in range(width):
                iUD[h-1-i,j] = image[i,j]
        return iUD
##对角镜像函数
def image_Amirror(file_path):
        image = cv_imread(file_path)
        height=image.shape[0]
        width=image.shape[1]
        h=height
        w=width
        size = (width,height)
        iAcross=copy.deepcopy(image)
        for i in range(height):
             for j in range(width):
                     iAcross[h-1-i,w-1-j] = image[i,j]
        return iAcross
   
for img_name in os.listdir(file_dir):
    img_name=img_name
    img_path = file_dir+img_name#读取每一个图片路径
    mirror_image=image_Lmirror(img_path)  ##水平镜像
    #mirror_image=image_Vmirror(img_path)  ##垂直镜像
    #mirror_image=image_Amirror(img_path)  ##对角镜像

    cv2.imwrite(dst+'qtmirrorverticle_364{:<d}.jpg'.format(i),mirror_image)  ##保存处理后的图像
    i+=1

print("图像处理完毕！")
