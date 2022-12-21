import cv2

img = cv2.imread('us.jpg')
grey = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
face = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = face.detectMultiScale(grey,1.1,5)

for x,y,w,h in faces:
    cv2.rectangle(img,(x,y),(x+w, y+h),(0,255,0),3)

cv2.imshow('face',img)
cv2.waitKey(0)
