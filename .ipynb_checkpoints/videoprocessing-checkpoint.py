#drawing on video
import cv2

#callback function to draw rectangle
def draw_rectangle(event,x,y,flags,param):
    global point1, point2, topLeft_clicked, bottomRight_clicked
    if event == cv2.EVENT_LBUTTONDOWN:
        
        #reset the rectangle if rectangle is here
        if topLeft_clicked == True and bottomRight_clicked == True:
            point1 = (0,0)
            point2 = (0,0)
            topLeft_clicked = False
            bottomRight_clicked = False
           
            
        if topLeft_clicked == False:
            point1 = (x,y)
            topLeft_clicked = True
            
        elif bottomRight_clicked == False:
            point2 = (x,y)
            bottomRight_clicked = True
            

#global variables

point1(0,0) #top left
point2 = (0,0) #bottom right

topLeft_clicked = False
bottomRight_clicked  False


#connect to callback
cv2.namedWindow('Test')
cv2.setMouseCallback('Test',draw_rectangle)


while True:
    ret, frame = capture.read()
    #draw on frame based off the global variables
    if topLeft_clicked:
        cv2.circle(frame,center = point1, radius = 3,
                   color = (0,0,255), thickness=-1)
        
    if topLeft_clicked and bottomRight_clicked:
        cv2.rectangle(frame,point1,point2,(0,0,255),3)
    
    cv2.imshow('Test',frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
        
capture.release()
cv2.destroyAllWindows()