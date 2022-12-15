import numpy as np
import cv2
from PIL import Image
import face_recognition

i=0
def save_face(frame, faces):
    global i
    for (top, right, bottom, left) in faces:
        i+=1
        # crop = frame[top:bottom, left:right]
        # cv2.rectangle(frame,(left,top),(right,bottom), (255, 0, 0), 2)
        # cv2.imwrite("file_crop{}.png".format(i),crop)
        cv2.imwrite("file{}.png".format(i),frame)
    return


camera = cv2.VideoCapture(0)

while (True):
    key = cv2.waitKey(1)
    ret, img = camera.read()
    if key==ord('q'):
        break
    elif key==ord('s'):
        save_face(img, face_locations)

    if ret:
        # Chuyen gray
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        face_locations = face_recognition.face_locations(img, number_of_times_to_upsample=1)
        # face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=4, model="cnn")
        # print("I found {} face(s) in this photograph.".format(len(face_locations)))
        img_draw = img
        for face_location in face_locations:
            # Print the location of each face in this image
            top, right, bottom, left = face_location
            # print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
            img_draw = cv2.rectangle(img_draw,(left,top),(right,bottom),(0,255,0),2)

        cv2.imshow("Picture", img_draw)


camera.release()
cv2.destroyAllWindows()
