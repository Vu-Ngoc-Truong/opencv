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

# Load a sample picture and learn how to recognize it.
person1_image = face_recognition.load_image_file("me.png")
person1_face_encoding = face_recognition.face_encodings(person1_image)[0]

# Load a second sample picture and learn how to recognize it.
person2_image = face_recognition.load_image_file("thanh.png")
person2_face_encoding = face_recognition.face_encodings(person2_image)[0]

# Create arrays of known face encodings and their names
known_face_encodings = [
    person1_face_encoding,
    person2_face_encoding
]
known_face_names = [
    "Mr. Truong",
    "Mr. Thanh"
]

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

        face_locations = face_recognition.face_locations(img,number_of_times_to_upsample=1)
        # face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=4, model="cnn")
        # print("I found {} face(s) in this photograph.".format(len(face_locations)))

        # Find all the faces and face encodings in the unknown image
        face_encodings = face_recognition.face_encodings(img, face_locations)

        img_draw = img
        for face_location, face_encoding in zip(face_locations, face_encodings):
            # Print the location of each face in this image
            top, right, bottom, left = face_location
            # print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
            img_draw = cv2.rectangle(img_draw,(left,top),(right,bottom),(0,255,0),2)
            # See if the face is a match for the known face(s)
            matches = face_recognition.compare_faces(known_face_encodings, face_encoding)

            name = "Unknown"
            face_distances = face_recognition.face_distance(known_face_encodings, face_encoding)
            best_match_index = np.argmin(face_distances)
            if matches[best_match_index]:
                name = known_face_names[best_match_index]
            (text_width, text_height) = cv2.getTextSize(name, cv2.FONT_HERSHEY_SIMPLEX,1,2)[0]
            # print(text_width)
            # print(text_height)
            cv2.rectangle(img_draw,(left,bottom),(right,bottom + text_height + 20),(255,100,0), -1)
            cv2.putText(img_draw, name, (left + 10, bottom + text_height + 10),cv2.FONT_HERSHEY_SIMPLEX, 0.8,(0,0,255), 2, cv2.LINE_AA)

        cv2.imshow("Picture", img_draw)


camera.release()
cv2.destroyAllWindows()
