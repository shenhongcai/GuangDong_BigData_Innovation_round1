import cv2
import os
import numpy as np



file_dir ='.\\source\\'
obj_dir='.\\result\\'

i=0

##对比度和亮度调整
def Contrast_and_Brightness(alpha, beta, img):
    blank = np.zeros(img.shape, img.dtype)
    # dst = alpha * img + beta * blank
    dst = cv2.addWeighted(img, alpha, blank, 1-alpha, beta)
    return dst


##旋转调整
def rotate(img,angle):  
    height = img.shape[0]  
    width = img.shape[1]  

    if angle%180 == 0:  
        scale = 1  
    elif angle%90 == 0:  
        scale = float(max(height, width))/min(height, width)  
    else:  
        scale = math.sqrt(pow(height,2)+pow(width,2))/min(height, width)  
    rotateMat = cv2.getRotationMatrix2D((width/2, height/2), angle, scale)  
    rotateImg = cv2.warpAffine(img, rotateMat, (width, height))  
    return rotateImg




def  cv_imread(filePath):
     cv_img=cv2.imdecode(np.fromfile(filePath,dtype=np.uint8),-1)
     return cv_img
    
for img_name in os.listdir(file_dir):
    img_name=img_name
    img_path = file_dir+img_name#读取每一个图片路径
    image = cv_imread(img_path)
    #rotate_image=rotate(image,180)
    image_brightened=Contrast_and_Brightness(1.020, 1.5, image)
    cv2.imwrite(obj_dir+'zd949Contrast_{:<d}.jpg'.format(i),image_brightened)
    i+=1
        
print("图像处理完毕！")
