import cv2

def read(event,x,y,flage,param):  
    if(event == cv2.EVENT_LBUTTONDBLCLK):  
        print(x,y)
        # cv2.circle(img,(x,y),100,(255,255, 0),-1)
        print(img[x][y])
        return x,y  

img=cv2.imread("Square/square492.jpg")
img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

cv2.namedWindow("IMG")
cv2.imshow("IMG",img)
cv2.setMouseCallback('IMG',read)

cv2.waitKey(0)


