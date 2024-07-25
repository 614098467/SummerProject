
import cv2


def Show(img,img_name = 'img'):
    cv2.imshow(img_name,img)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


img_gray = cv2.imread('cat.jpg',cv2.IMREAD_GRAYSCALE)




ret,thresh1 = cv2.threshold(img_gray,127,255,type=cv2.THRESH_TOZERO_INV)

blur = cv2.blur(img_gray,(3,3))

box = cv2.boxFilter(img_gray,-1,(3,3),normalize=True)

Gauss = cv2.GaussianBlur(img_gray,(5,5),1)

print(img_gray.shape)
mean = cv2.medianBlur(img_gray,3)
Show(mean)



