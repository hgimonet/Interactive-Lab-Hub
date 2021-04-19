'''
Based on https://opencv-python-tutroals.readthedocs.io/en/latest/py_tutorials/py_objdetect/py_face_detection/py_face_detection.html#face-detection

Look here for more cascades: https://github.com/parulnith/Face-Detection-in-Python-using-OpenCV/tree/master/data/haarcascades


Edited by David Goedicke
'''


import numpy as np
import cv2
import sys

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')


img=None
webCam = False
if(len(sys.argv)>1):
   try:
      print("I'll try to read your image");
      img = cv2.imread(sys.argv[1])
      if img is None:
         print("Failed to load image file:", sys.argv[1])
   except:
      print("Failed to load the image are you sure that:", sys.argv[1],"is a path to an image?")
else:
   try:
      print("Trying to open the Webcam.")
      cap = cv2.VideoCapture(0)
      if cap is None or not cap.isOpened():
         raise("No camera")
      webCam = True
   except:
      img = cv2.imread("../data/test.jpg")
      print("Using default image.")


while(True):
   if webCam:
      ret, img = cap.read()

   gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

   faces = face_cascade.detectMultiScale(gray, 1.3, 5)
   for (x,y,w,h) in faces:
       img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
       roi_gray = gray[y:y+h, x:x+w]
       roi_color = img[y:y+h, x:x+w]
       eyes = eye_cascade.detectMultiScale(roi_gray)
       for (ex,ey,ew,eh) in eyes:
           cv2.rectangle(roi_color,(ex,ey),(ex+ew,ey+eh),(0,255,0),2)

   if webCam:
      cv2.imshow('face-detection (press q to quit.)',img)
      if cv2.waitKey(1) & 0xFF == ord('q'):
         cap.release()
         break
   else:
      break

cv2.imwrite('faces_detected.jpg',img)
cv2.destroyAllWindows()

