import numpy as np
import cv2
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
face_cascade = cv2.CascadeClassifier(dir_path + '/haarcascade_frontalface_default.xml')
print(dir_path)
# print(face_cascade)
# face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')



# camera = cv2.VideoCapture(0)

# while (True):
# ret, img = camera.read()
img = cv2.imread(dir_path+ "/cdt_4.jpg")

# Chuyen gray
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = face_cascade.detectMultiScale(gray, 1.2, 10,minSize=(100,100))
print("xong")
print("num of face:", len(faces))
for (x, y, w, h) in faces:
    cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
    qroi_color = img[y:y + h, x:x + w]

# cv2.imshow("Picture", img)

key = cv2.waitKey(0)
# if key==ord('q'):
#     break
# elif key==ord('s'):
#     save_face(img, faces)

# camera.release()
cv2.destroyAllWindows()
