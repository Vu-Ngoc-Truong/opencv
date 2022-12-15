from PIL import Image
import face_recognition
import cv2
import os

dir_path = os.path.dirname(os.path.realpath(__file__))
print(dir_path)
# /home/ngoctruong/code_ws/Python/library_basic/opencv/face_indent
pkg_path = os.path.dirname(dir_path)
print(pkg_path)
# /home/ngoctruong/code_ws/Python/library_basic/opencv


# Load the jpg file into a numpy array
# image = face_recognition.load_image_file("me.png")
img_path = os.path.join(dir_path, "image_test", "cdt_4.jpg")
print(img_path)

image = cv2.imread(img_path)
image_cvt = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Find all the faces in the image using a pre-trained convolutional neural network.
#  use hog model
face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=4)
#  use cnn model
# face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=4, model="cnn")
print(face_locations)

print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    # print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
    img = cv2.rectangle(image,(left,top),(right,bottom),(0,255,0),2)

cv2.imshow('Image', image)
key = cv2.waitKey(0)
cv2.destroyAllWindows()
