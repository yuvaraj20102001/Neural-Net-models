import cv2 
import numpy as np


# capture = cv2.VideoCapture("footage.mp4")

# while(1):
#     ret,frame = capture.read()
#     # cv2.imshow("video",frame)
#     frame=cv2.resize(frame,(500,500))
#     hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
#     lower = (50, 100, 100)
#     upper = (70, 255, 255)
#     inrange_hsv=cv2.inRange(hsv,lower,upper)
#     cv2.imshow("inrange_hsv",inrange_hsv)
#     print(inrange_hsv.shape,frame.shape)
#     # bitwise_and=cv2.bitwise_or(frame,inrange_hsv)
#     # cv2.imshow("bitwise",bitwise_and)
#     cv2.imshow("hsv",hsv)
#     cv2.imshow("video",frame)
#     if cv2.waitKey(1) & 0xFF == ord('q'):
#         break
# capture.release()
# # print(inrange_hsv)
# cv2.destroyAllWindows()


test=np.zeros((50,50))
test=cv2.circle(test,(10,10),radius=50,color=(255,255,255))
cv2.imshow("test",test)
cv2.waitKey(0)