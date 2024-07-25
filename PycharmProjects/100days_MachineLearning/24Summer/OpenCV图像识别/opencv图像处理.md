# 图像处理

# 1 常用操作
## 1.1 图像读取
cv2.imrear('文件名'，参数可选)

1. cv2.IMREAD_COLOR  读取彩色图像
2. cv2.IMREAD_GRAYSCALE 读取灰色图像


    img_color = cv2.imread('cat.jpg',cv2.IMREAD_COLOR)
    img_Gray = cv2.imread('cat.jpg',cv2.IMREAD_GRAYSCALE)

## 1.2 图像的保存
cv2.imwrite('文件名',图像)

    cv2.imwrite('cat_gary.jpg',img_Gray)
## 1.3 图像的展示

    def Show(img,name = 'img'):
        cv2.imshow(name,img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

## 1.4 截取图像的部分区域ROI
因为图像的格式为np.array(),可以通过截取数组的方式获得部分图像

    img_ROI = img_color[0:50,100:200]

## 1.5 RGB通道的提取
因为opencv读取图像时候的数组表示是b,g,r格式，使用cv2.split(图像)来读取通道
或者直接将数组的第三维度变为0。
方法一：
        
    b,g,r = cv2.split(img)

方法二：
    
    img[:,:,0] = 1 // 设置第一通道为0
## 1.6 边界的填充
首先需要规定图像边界上下左右的距离在进行填充，边界填充有5种方法,使用cv2.copyMakerBorder()来进行填充。
1. cv2.BORDER_REPLICATE
2. cv2.BORDER_REFLECT
3. cv2.BORDER_REFLECT_101
4. cv2.BORDER_WRAP
5. cv2.BORDER_CONSTANT


    top_size,bottom_size,left_size,right_size = (50,50,50,50)
    replicate = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REPLICATE)
    reflect = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REFLECT)
    reflect101 = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_REFLECT_101)
    wrap = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_WRAP)
    constant = cv2.copyMakeBorder(img,top_size,bottom_size,left_size,right_size,borderType=cv2.BORDER_CONSTANT,value=100)

## 1.7 数值计算
使用cv2.resize(width,height) 来调整图像的尺寸。
使用cv2.addWeighted(图像1，1的系数，图像2，2的系数，偏执项(一般为0))


    img1 = cv2.imread('cat.jpg')
    img2 = cv2.imread('dog.jpg')
    
    cv3 = cv2.addWeighted(img1,0.4,img2,0.6,0)

# 2 阈值与平滑处理

## 2.1 通过阈值过滤图
ret,dst = cv2.threshold(src,thresh,maxvalue,type)

- src： 输入图，只能输入单通道图像，通常来说为灰度图
- dst： 输出图
- thresh： 阈值
- maxval： 当像素值超过了阈值（或者小于阈值，根据type来决定），所赋予的值
- type：二值化操作的类型，包含以下5种类型： cv2.THRESH_BINARY； cv2.THRESH_BINARY_INV； cv2.THRESH_TRUNC； cv2.THRESH_TOZERO；cv2.THRESH_TOZERO_INV

- cv2.THRESH_BINARY           超过阈值部分取maxval（最大值），否则取0
- cv2.THRESH_BINARY_INV    THRESH_BINARY的反转
- cv2.THRESH_TRUNC            大于阈值部分设为阈值，否则不变
- cv2.THRESH_TOZERO          大于阈值部分不改变，否则设为0
- cv2.THRESH_TOZERO_INV  THRESH_TOZERO的反转


        ret,dst = cv2.threshold(img_gray,127,255,type = cv2.THRESH_BINARY_INV)

## 2.2 平滑处理
平滑处理就是在图中选择一个矩阵，对矩阵中的数字进行重新计算然后赋值给中间。

#### 均值滤波：求得均值然后赋值给中间
cv2.blur(图像,(矩阵大小))
        
    blur = cv2.blur(img_gray,(3,3))
#### 方框滤波：和均值相同，但是可以选择归一化
cv2.boxFilter(图像，-1,(矩阵大小)，normalize = True)

    box = cv2.boxFilter(img_gray,-1,(3,3),normalize=True)
#### 高斯滤波：距离中心近的权重越大，越远的权重越小,更加重视中间值
    Gauss = cv2.GaussianBlur(img_gray,(5,5),1)
### 中值滤波：直接取中值进行滤波
    mean = cv2.medianBlur(img_gray,3)

# 3 形态学操作
## 3.1 腐蚀操作 cv2.erode
    
    kernel = np.ones((3,3),dtype=np.uint8)
    erosion = cv2.erode(dige_img,kernel,iterations=3)

## 3.2 膨胀操作 cv2.dilate
    
    kernel = np.ones((3,3),dtype=np.uint8)
    dilate = cv2.dilate(dige_img,kernel,iterations=3)

## 3.3 开运算和闭运算 cv2.morphologyEX
开运算：先腐蚀再膨胀。
    
    opening = cv2.morphologyEx(dige_img,cv2.MORPH_OPEN,kernel=kernel)

闭运算：先膨胀再腐蚀。

    closing = cv2.morphologyEx(dige_img,cv2.MORPH_CLOSE,kernel=kernel)
## 3.4 梯度运算
梯度 = 膨胀 - 腐蚀
    
    gradient = cv2.morphologyEx(dige_img,cv2.MORPH_GRADIENT,kernel=kernel)
## 3.5 礼帽和黑帽
礼帽 = 原始输入 - 开运算结果。
    
    tophat = cv2.morphologyEx(dige_img,cv2.MORPH_TOPHAT,kernel=kernel)
黑帽 = 闭运算结果 - 原始输入
    
    blackhat = cv2.morphologyEx(dige_img,cv2.MORPH_BLACKHAT,kernel=kernel)

# 4 梯度计算

## 4.1 Sobel算子

Gx = [[-1,0,1],
      [-2,0,2],
      [-1,0,1]]

Gy = [[-1,-2,-1],
      [0,0,0],
      [1,2,1]]

    sobelx = cv2.Sobel(sphere_img,cv2.CV_64F,1,0,ksize=3)
    sobelx = cv2.convertScaleAbs(sobelx)
    
    sobely = cv2.Sobel(sphere_img,cv2.CV_64F,0,1,ksize=3)
    sobely = cv2.convertScaleAbs(sobely)
## 4.2 梯度计算方法

    sobelxy = cv2.addWeighted(sobelx,0.5,sobely,0.5,0)



## 4.3 Scharr算子 和 Laplacian 算子

Scharr Gx = [[-3,0,3],
          [-10,0,10],
          [-3,0,3]]
Scharr Gy = [[-3,-10,-3],
            [0,0,0],
            [-3,-10,-3]]       

    scharrx = cv2.Scharr(sphere_img,cv2.CV_64F,1,0)
    scharrx = cv2.convertScaleAbs(scharrx)
    scharry = cv2.Scharr(sphere_img,cv2.CV_64F,0,1)
    scharry = cv2.convertScaleAbs(scharry)
    scharrXY = cv2.addWeighted(scharrx,0.5,scharry,0.5,0)
Laplacian = [[0,1,0],
             [1,-4,1],
             [0,1,0]]
    
    laplacian = cv2.Laplacian(sphere_img,cv2.CV_64F)
    laplacian = cv2.convertScaleAbs(laplacian)


# 5 边缘检测
## 5.1 Canny边缘检测
1. 使用高斯滤波器，平滑图像，滤波噪声
2. 计算图像中每个像素点的梯度强度和方向
3. 应用非极大值抑制，消除边缘检测带来的杂散影响
4. 应用双阈值检测来确定真实和潜在的边缘
5. 通过抑制孤立的弱边缘来完成边缘检测

### 非极大值抑制
比较梯度方向上，当前的点和两侧相邻的点的梯度，保留最大的梯度，并且丢弃周围的梯度。

### 双阈值检测
设置梯度的最大值和最小值，超过最大值的梯度，都保留并且设为边界。如果梯度在最大值和最小值之间，如果该点连接边界，则保留，如果左右两边没有连接
边界，则舍弃。

# 6 图像金字塔与轮廓的检测





