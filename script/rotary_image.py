# import the necessary packages
import argparse
import imutils
import cv2
import numpy  as np
# # construct the argument parser and parse the arguments
# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", type=str, default="logo.png",
# 	help="path to the input image")
# args = vars(ap.parse_args())

# load the image and show it
image = cv2.imread("office1.png")
cv2.imshow("Original", image)
# grab the dimensions of the image and calculate the center of the
# image
(h, w) = image.shape[:2]
(cX, cY) = (w // 2, h // 2)
# rotate our image by 45 degrees around the center of the image
M = cv2.getRotationMatrix2D((cX, cY), 37, 1.0)
M = np.float([
	[1, 0, 25],
	[0, 1, 50]
])
print(M)
rotated = cv2.warpAffine(image, M, (w, h))
cv2.imshow("Rotated by 45 Degrees", rotated)
cv2.imwrite('map_rotate_cv2.png', rotated)
# # rotate our image by -90 degrees around the image
# M = cv2.getRotationMatrix2D((cX, cY), -90, 1.0)
# rotated = cv2.warpAffine(image, M, (w, h))
# cv2.imshow("Rotated by -90 Degrees", rotated)
ret,thresh_binary = cv2.threshold(rotated,200,255,cv2.THRESH_BINARY)
cv2.imshow("Rotated and thresh", thresh_binary)
cv2.imwrite('map_rotate_cv2_thresh.png', thresh_binary)
cv2.waitKey(0)

cv2.destroyAllWindows()