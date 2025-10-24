import numpy as np
import cv2
import os

def perspective(frame , x = None ,y = None ,w = None ,h = None):
    if x != None and y!= None and w != None and h != None:
        p1 = np.array(([x,y],
                [x+w , y],
                [x, y+h],
                [x+w, y+h]), 
                dtype= np.float32)
    else:
        x = 0
        y = 0
        w = frame.shape[1]
        h = frame.shape[0]
        p1 = np.array(([x,y],
                [x+w , y],
                [x, y+h],
                [x+w, y+h]), 
                dtype= np.float32)
        
    p2 = np.array(([0,0], 
                [250,0],
                [0,300] ,
                [250,300]), 
                dtype=np.float32)

    t = cv2.getPerspectiveTransform(p1,p2)
    tug = cv2.warpPerspective(frame , t , (250,300))
    return tug

def Blur(image , blur_value , x=None , y= None , w = None , h = None):
    if x != None or y != None or w != None or h != None :
        image = cv2.medianBlur(image[y:y+h , x:x+w] , blur_value)
        return image
    else:
        image = cv2.medianBlur(image , blur_value)
        return image   
    
def findBorders(img):
    gimg = cv2.cvtColor(img , cv2.COLOR_BGR2GRAY)
    cimg = cv2.Canny(gimg , 125 , 175 ,10)
    count , _ = cv2.findContours(cimg , cv2.RETR_EXTERNAL , cv2.CHAIN_APPROX_SIMPLE)
    
    max_contour = max(count , key = cv2.contourArea) 
    x, y , w, h = cv2.boundingRect(max_contour)
    
    return x, y , w, h

def savepic(img , name):
    os.makedirs("PIC" , exist_ok=True)
    path = os.path.join("PIC", f"__{name}.jpg")
    cv2.imwrite(path , img)
    print(f"photo__{name} saved at PIC!")