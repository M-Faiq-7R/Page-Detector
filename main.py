# 1. Capture: Take clear, well-lit photos of A4 documents with your phone.
# 2. Preprocess: Convert to grayscale and apply Gaussian blur to reduce noise.
# 3. Edge Detection: Use Canny to highlight document boundaries.
# 4. Contour Detection: Find contours and select the largest quadrilateral (the document).
# 5. Corner Ordering: Arrange detected corners in top-left, top-right, bottom-right, bottom-left order.
# 6. Perspective Transform: Warp the quadrilateral to a flat A4 rectangle.
# 7. Save: Export the final extracted document as a PNG

import cv2
import private as i


cap = cv2.VideoCapture('vid1.mp4')
passes = 0
while True:
    ret, frame = cap.read()
    if not  ret:
        print("No File!")
        break
    else:
        frame = cv2.resize(frame, (250,300))
        cframe = frame.copy()
        cv2.imshow("Image" , frame)
        frame = i.Blur(frame , 9)
        gframe = cv2.cvtColor(frame , cv2.COLOR_BGR2GRAY)
        _ , thresh = cv2.threshold(gframe, 125 , 255, cv2.THRESH_BINARY)
        iframe = i.perspective(frame)
        x, y, w, h = i.findBorders(iframe)
        roi = i.perspective(cframe , x , y, w ,h)
        i.savepic(roi , passes)
        passes += 1
        cv2.rectangle(iframe , (x,y), (x+w , y+h) , (0,255,0) , 3)
        
        cv2.imshow("ROI" , roi)
        cv2.imshow("I-Frame", iframe)
        cv2.imshow("Thresh" , thresh)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break



cv2.waitKey(0)

cv2.destroyAllWindows()
