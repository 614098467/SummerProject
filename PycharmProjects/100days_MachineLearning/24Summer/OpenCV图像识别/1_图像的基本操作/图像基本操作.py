import cv2
import matplotlib.pyplot as plt


img = cv2.imread('cat.jpg')


def Show(img,name = 'img'):
    cv2.imshow(name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

## 彩色图像和灰度图像
img_color = cv2.imread('cat.jpg',cv2.IMREAD_COLOR)
img_Gray = cv2.imread('cat.jpg',cv2.IMREAD_GRAYSCALE)

# Show('cat_gary',img_Gray)

## 保存
# cv2.imwrite('cat_gary.jpg',img_Gray)

## 视频读取
#
# def transforerToGray(filename):
#     video = cv2.VideoCapture(filename)
#     if video.isOpened():
#         open,frame = video.read()
#     else:
#         open = False
#
#     while open:
#         ret,frame = video.read()
#         if frame is None:
#             break
#         if ret == True:
#             gray = cv2.cvtColor(frame,cv2.COLOR_BGR2YCrCb)
#             cv2.imshow('result',gray)
#             if cv2.waitKey(1) & 0xFF == 27:
#                 break
#     video.release()
#     cv2.destroyAllWindows()
#
# transforerToGray('test.mp4')

## ROI 截取图像部分区域

# img_ROI = img_color[0:50,100:200]
# Show('catROI',img_ROI)

## 颜色通道的提取
# b,g,r = cv2.split(img_color)
# R_img = img_color.copy()
# R_img[:,:,1] = 0
# R_img[:,:,2] = 0
#
# cv2.merge((b,g,r))
# Show('carR',R_img)

## 边界填充
# top_size,bottom_size,left_size,right_size = (50,50,50,50)
# replicate = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REPLICATE)
# reflect = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REFLECT)
# reflect101 = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REFLECT_101)
# wrap = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_WRAP)
# constant = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_CONSTANT,value=100)
#
#
# plt.subplot(231),plt.imshow(img,'gray'),plt.title('Original')
# plt.subplot(232),plt.imshow(replicate,'gray'),plt.title('img_replicate')
# plt.subplot(233),plt.imshow(reflect,'gray'),plt.title('img_reflect')
# plt.subplot(234),plt.imshow(reflect101,'gray'),plt.title('img_reflect101')
# plt.subplot(235),plt.imshow(wrap,'gray'),plt.title('img_wrap')
# plt.subplot(236),plt.imshow(constant,'gray'),plt.title('img_constant')
# plt.show()





#### 数值计算

img += 10

img2 = cv2.imread('face.jpg')
img2 = cv2.resize(img2,(500,414))


img3 = cv2.addWeighted(img,0.3,img2,0.7,0)

print(img.shape,img2.shape)

Show(img3)

