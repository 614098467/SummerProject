import cv2
import numpy as np
def Show(img,img_name = 'img'):
    cv2.imshow(img_name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


dige_img = cv2.imread('dige.png')

# Show(dige_img)

## 腐蚀
kernel = np.ones((3,3),dtype=np.uint8)
erosion = cv2.erode(dige_img,kernel,iterations=3)


combine = np.hstack((dige_img,erosion))
print(erosion)


## 膨胀
kernel = np.ones((3,3),dtype=np.uint8)
dilate = cv2.dilate(dige_img,kernel,iterations=3)

## 开运算 = 先腐再膨胀

opening = cv2.morphologyEx(dige_img,cv2.MORPH_OPEN,kernel=kernel)
closing = cv2.morphologyEx(dige_img,cv2.MORPH_CLOSE,kernel=kernel)

## 梯度计算
gradient = cv2.morphologyEx(dige_img,cv2.MORPH_GRADIENT,kernel=kernel)


## 礼帽和黑帽

tophat = cv2.morphologyEx(dige_img,cv2.MORPH_TOPHAT,kernel=kernel)

blackhat = cv2.morphologyEx(dige_img,cv2.MORPH_BLACKHAT,kernel=kernel)

Show(tophat)
Show(blackhat)

##
