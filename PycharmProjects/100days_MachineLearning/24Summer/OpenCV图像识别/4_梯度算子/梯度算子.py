
import cv2

def Show(img,img_name = 'img'):
    cv2.imshow(img_name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


sphere_img = cv2.imread('pie.png')

## Sobel算子
sobelx = cv2.Sobel(sphere_img,cv2.CV_64F,1,0,ksize=3)
sobelx = cv2.convertScaleAbs(sobelx)


sobely = cv2.Sobel(sphere_img,cv2.CV_64F,0,1,ksize=3)
sobely = cv2.convertScaleAbs(sobely)

##梯度计算方法
sobelxy = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)


## Scharr

scharrx = cv2.Scharr(sphere_img,cv2.CV_64F,1,0)
scharrx = cv2.convertScaleAbs(scharrx)
scharry = cv2.Scharr(sphere_img,cv2.CV_64F,0,1)
scharry = cv2.convertScaleAbs(scharry)
scharrXY = cv2.addWeighted(scharrx,0.5,scharry,0.5,0)
Show(scharrXY)

## Laplacian
laplacian = cv2.Laplacian(sphere_img,cv2.CV_64F)
laplacian = cv2.convertScaleAbs(laplacian)
Show(laplacian)

