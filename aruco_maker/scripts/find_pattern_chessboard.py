import numpy as np
import cv2 as cv
import glob
# termination criteria
criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)
# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)
# print("mgrid : \n", np.mgrid[0:7,0:6].T.reshape(-1,2))
print(objp.shape)
# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.
# load image
images = glob.glob('../img/*.jpg')
print("load img complete")
count_img = 0

# load video
video_capture = cv.VideoCapture(0)

while True:
    # Grab a single frame of video
    ret, frame = video_capture.read()
    img = frame
# for fname in images:
    # img = cv.imread(fname)
    gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
    # Find the chess board corners
    ret, corners = cv.findChessboardCorners(gray, (8,6), None)
    # If found, add object points, image points (after refining them)
    if ret == True:
        # objpoints.append(objp)
        corners2 = cv.cornerSubPix(gray,corners, (5,5), (-1,-1), criteria)
        # imgpoints.append(corners)
        # Draw and display the corners
        cv.drawChessboardCorners(img, (7,6), corners2, ret)
    cv.imshow('img', img)
    if cv.waitKey(1) & 0xFF == ord('q'):
        break
        # count_img +=1
# print("objpoints: \n", objpoints[1][2])
# print(count_img)
# print("imgpoints: \n", imgpoints)

# Release handle to the webcam
video_capture.release()
cv.destroyAllWindows()