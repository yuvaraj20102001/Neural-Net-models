
import cv2
import numpy as np
import matplotlib.pyplot as plt

# ''' CIRCLE '''
white=[255,255,255]

# color_palaette=np.random.randint(50,255,(500,3))
# R,G,B=color_palaette[:,0],color_palaette[:,1],color_palaette[:,2]

# center=np.random.randint(70,350,(1000,2))
# radius=np.random.randint(25,100,1000)
# print(color_palaette)


# for i in range(500,1000):
#     background=np.zeros((500,500,3),dtype=np.uint8)
#     print(center[i])
#     R,G,B=np.random.randint(10,255),np.random.randint(10,255),np.random.randint(10,255)

#     cv2.circle(background,center[i],radius[i],[R,G,B],thickness=-1)
#     cv2.imwrite(f"Circle/circle{i}.jpg".format(i),background)

#     # cv2.imshow("img",background)
#     cv2.waitKey(0)


''' SQUARE '''

# pt1=np.random.randint(30,270,(1000,2))
# size=np.random.randint(50,250,1000)
# center=(500//2,500//2)
# for i in range(500,1000):
#     background=np.zeros((500,500),dtype=np.uint8)
#     print(pt1[i])
#     print(size[i])
#     pt2=pt1[i]+size[i]
#     cv2.rectangle(background,pt1[i],pt2,color=[255,255,255],thickness=-1)
#     # cv2.imshow("img1",background)

#     angle=np.random.randint(0,181)
#     print(angle)
#     scale=np.random.uniform(0.5,1.0)
#     rotmat=cv2.getRotationMatrix2D(center,angle,scale=1)
    
#     background=cv2.warpAffine(background,rotmat,(500,500))

#     contours,hierarchy=cv2.findContours(background,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#     # print(len(contours))
#     # print(contours)

#     R,G,B=np.random.randint(10,255),np.random.randint(10,255),np.random.randint(10,255)
#     new_background=np.ones((500,500,3),dtype=np.uint8)*255

#     cv2.drawContours(new_background,contours,-1,thickness=cv2.FILLED,color=[R,G,B])


#     # R,G,B=np.random.randint(10,255),np.random.randint(10,255),np.random.randint(10,255)

#     # new_background=np.ones((500,500,3),dtype=np.uint8)*255
#     cv2.imwrite(f"Square/square{i}.jpg".format(i),new_background)
#     # print(cv2.imwrite(f"square{i}.jpg".format(i),new_background))
#     # np.where(background==[0,0,0],background+255,background)
#     # cv2.imshow("img",background)
#     # cv2.imshow("img2",new_background)
#     cv2.waitKey(0)





''' STAR '''


# for i in range(500,1000):
#     x1=np.random.randint(100,350)
#     y1=np.random.randint(100,350)
#     x2,y2=x1+100,y1+100
#     x3,y3=x2-150,y2-10
#     x4,y4=x3+150,y3-60
#     x5,y5=x4-100,y4+120
#     background=np.zeros((500,500,3),dtype=np.uint8)

#     cv2.line(background,(x1,y1),(x2,y2),thickness=3,color=white)
#     cv2.line(background,(x2,y2),(x3,y3),thickness=3,color=white)
#     cv2.line(background,(x3,y3),(x4,y4),thickness=3,color=white)
#     cv2.line(background,(x4,y4),(x5,y5),thickness=3,color=white)
#     cv2.line(background,(x5,y5),(x1,y1),thickness=3,color=white)
#     # cv2.imshow("org_img",background)
    
#     # x,background_thresh=cv2.threshold(background_gray,200,255,cv2.THRESH_BINARY)

#     angle=np.random.randint(20,90) 
#     # print(angle)
#     scale=np.random.uniform(0.5,1)
    
#     rot_mat=cv2.getRotationMatrix2D((500//2,500//2),angle,scale)
#     background=cv2.warpAffine(background,rot_mat,(500,500))
#     background_gray=cv2.cvtColor(background,cv2.COLOR_BGR2GRAY)
#     # cv2.imshow("org_gray_img",background_gray)
#     contours,hierarchy=cv2.findContours(background_gray,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
#     # print(len(contours))
#     print(contours)

#     R,G,B=np.random.randint(10,255),np.random.randint(10,255),np.random.randint(10,255)
#     new_background=np.zeros((500,500,3),dtype=np.uint8)
#     cv2.drawContours(new_background,contours,-1,thickness=cv2.FILLED,color=[R,G,B])


#     # cv2.imshow("contourss",new_background)
#     # x,background=cv2.threshold(background,50,255,cv2.THRESH_BINARY_INV)

#     # cv2.imshow("contour_img",new_background)
#     cv2.imwrite(f"Star/star{i}.jpg".format(i),new_background)
#     # cv2.imshow("img",background)

#     cv2.waitKey(0)




"""Pentagon """



# for i in range(500,1000):
#     x1=np.random.randint(120,350)
#     y1=np.random.randint(120,350)
#     x2,y2=x1+50,y1-50
#     x3,y3=x2+50,y2+50
#     x4,y4=x3-25,y3+50
#     x5,y5=x4-50,y4
#     background=np.zeros((500,500,3),dtype=np.uint8)
#     pts=np.array([[x1,y1],[x2,y2],[x3,y3],[x4,y4],[x5,y5]],dtype=np.int32).reshape((-1, 1, 2))
#     # cv2.line(background,(x1,y1),(x2,y2),thickness=1,color=white)
#     # cv2.line(background,(x2,y2),(x3,y3),thickness=1,color=white)
#     # cv2.line(background,(x3,y3),(x4,y4),thickness=1,color=white)
#     # cv2.line(background,(x4,y4),(x5,y5),thickness=1,color=white)
#     # cv2.line(background,(x5,y5),(x1,y1),thickness=1,color=white)
#     cv2.fillPoly(background,[pts],(255,255,255))
#     background_gray=cv2.cvtColor(background,cv2.COLOR_BGR2GRAY)
#     x,background_thresh=cv2.threshold(background_gray,0,255,cv2.THRESH_BINARY)
  
#     angle=np.random.randint(20,180)
#     print(angle)
#     scale=np.random.uniform(0.8,1.8)
  
#     rot_mat=cv2.getRotationMatrix2D((500//2,500//2),angle,scale)
#     background_thresh=cv2.warpAffine(background_thresh,rot_mat,(500,500))
#     # cv2.imshow("img",background_thresh)
#     contours,hierarchy=cv2.findContours(background_thresh,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#     new_background=np.ones((500,500,3),dtype=np.uint8)*255

#     R,G,B=np.random.randint(10,255),np.random.randint(10,255),np.random.randint(10,255)

#     cv2.drawContours(new_background,contours,-1,thickness=-1,color=[R,G,B])
#     cv2.imwrite(f"Pentagon/pentagon{i}.jpg".format(i),new_background)

#     cv2.imshow("base",new_background)
#     # cv2.imshow("img",background)

#     cv2.waitKey(0)



"""TRIANGLE"""



# for i in range(500,1000):
#     x1=np.random.randint(100,350)
#     y1=np.random.randint(100,350)
#     x2,y2=x1+50,y1-50
#     x3,y3=x2+50,y2+50
#     pts=np.array([[x1,y1],[x2,y2],[x3,y3]],dtype=np.int32).reshape((-1, 1, 2))
#     print(pts.squeeze())

#     background=np.zeros((500,500,3),dtype=np.uint8)

#     # cv2.line(background,(x1,y1),(x2,y2),thickness=3,color=white)
#     # cv2.line(background,(x2,y2),(x3,y3),thickness=3,color=white)
#     # cv2.line(background,(x3,y3),(x1,y1),thickness=3,color=white)
#     cv2.fillPoly(background,[pts],(255,255,255))
#     # cv2.polylines(background,pts,isClosed=True,color=[233,0,0],thickness=3)
#     angle=np.random.randint(20,180)
#     print(angle)
#     scale=np.random.uniform(0.8,1.5)
 
#     rot_mat=cv2.getRotationMatrix2D((500//2,500//2),angle,scale)
#     background=cv2.warpAffine(background,rot_mat,(500,500))
#     background_gray=cv2.cvtColor(background,cv2.COLOR_BGR2GRAY)
  

#     # cv2.imshow("img",background_thresh)
#     contours,hierarchy=cv2.findContours(background_gray,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
#     # new_background=np.ones((500,500,3),dtype=np.uint8)*255
#     R,G,B=np.random.randint(10,255),np.random.randint(10,255),np.random.randint(10,255)

#     cv2.drawContours(background,contours,-1,thickness=-1,color=[R,G,B])
    
#     cv2.imwrite(f"Triangle/triangle{i}.jpg".format(i),background)
    
#     # cv2.imshow("base",new_background)
#     cv2.imshow("img",background)
#     cv2.waitKey(0)
 