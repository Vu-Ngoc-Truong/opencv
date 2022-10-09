from PIL import Image
import face_recognition
import cv2
# Load the jpg file into a numpy array
# image = face_recognition.load_image_file("me.png")
image = cv2.imread("cdt1.png")
image_cvt = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# Find all the faces in the image using a pre-trained convolutional neural network.
face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=4)
# face_locations = face_recognition.face_locations(image, number_of_times_to_upsample=4, model="cnn")
# print(face_locations)

# cv2.imshow('Lop CDT1-K2', image_gray)
# cv2.waitKey(0)
# cv2.destroyWindow('image')
print("I found {} face(s) in this photograph.".format(len(face_locations)))

for face_location in face_locations:

    # Print the location of each face in this image
    top, right, bottom, left = face_location
    # print("A face is located at pixel location Top: {}, Left: {}, Bottom: {}, Right: {}".format(top, left, bottom, right))
    img = cv2.rectangle(image,(left,top),(right,bottom),(0,255,0),2)

cv2.imshow('Image', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
