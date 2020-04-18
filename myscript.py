import cv2
import numpy as np
#draw red cirle for every right mouse click event
def draw_circle(event,x,y,flags,param):
    if event == cv2.EVENT_RBUTTONDOWN:
        cv2.circle(img_draw,(x,y),100,(0,0,255),thickness=10)

img_draw= cv2.imread('DATA/dog_backpack.png')        
cv2.namedWindow(winname='Draw-Circles')

#connect to call-back
cv2.setMouseCallback('Draw-Circles',draw_circle)


#Show image in window

while True:
    cv2.imshow('Draw-Circles',img_draw)
    if cv2.waitKey(20) & 0xFF==27:
        break
cv2.destroyAllWindows()