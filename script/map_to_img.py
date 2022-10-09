import cv2
import numpy as np
import os
import time
import sys
import rospy
import yaml
from nav_msgs.msg import OccupancyGrid
from nav_msgs.srv import GetMap
from PIL import Image, ImageFilter  # Import classes from the library.
import imutils

# print(cv2.__version__)
# Function


def get_map():
    rospy.wait_for_service("static_map")
    print("map service on")
    try:

        get_map_raw = rospy.ServiceProxy("static_map", GetMap)
        resp1 = get_map_raw()

        map_arr = np.array(resp1.map.data)
        for i in range(len(map_arr)):
            if map_arr[i] == -1:
                map_arr[i] = 100
            elif map_arr[i] == 0:
                map_arr[i] = 255
            elif map_arr[i] >= 100:
                map_arr[i] = 10
            # else:
            #     map_arr[i] = 1

        map_arr = np.array(map_arr, dtype=np.uint8)
        return map_arr.reshape(resp1.map.info.height, resp1.map.info.width)
        # return resp1.map.data
    except rospy.ServiceException as e:
        print("Service call failed: %s" % e)


# Subscriber
# rospy.Subscriber('/map', OccupancyGrid , load_map_cb)


rospy.init_node("load_map")
rospy.loginfo("Init node: %s" % rospy.get_name())
# rospy.spin()
map_raw = get_map()
# print(map_raw.shape)
# print(map_raw)
# map_img = np.array(map_raw)
# print(type(map_img))
# print(len(map_img))
cv2.imwrite("map_img.jpg", map_raw)
# cv2.imshow('map image', map_raw)
# cv2.waitKey(0)

# img  = cv2.imread('logo.png')
# img_gray = cv2.imread('logo.png', cv2.IMREAD_GRAYSCALE)
# print('img_gray')
# print(img_gray.shape)
# print(img_gray)
# print(img)

# b = np.zeros([200,250,3])
# c = np.ones([100,100])
# for i in range(30,70):
#     for j in range(30,70):
#         if j<= i :
#             c[i,j] = 250

# b[:,:,0] = np.ones([200,250])*1
# b[:,:,1] = np.ones([200,250])*1
# b[:,:,2] = np.ones([200,250])*200

# cv2.imwrite('color_img.jpg', b)
# cv2.imwrite('gray_img.jpg', c)
# cv2.imshow('Color image', b)

# original_image = Image.open("map_img.jpg") # Load an image from the file system.
# img  = cv2.imread('map_img.jpg')
# # Display both images.
# # original_image.show()

# rotated_image = original_image.rotate(55) # Rotate the image by 180 degrees.
# # Xoay
# rotated = imutils.rotate(img, 55)
# cv2.imwrite('rotate_imu.jpg', rotated)
# cv2.imshow("rotate_imu", rotated)

# rotated_image.save("rotated_img.png") # Save the rotated image.
# rotated_image.show()
# cv2.waitKey(0)

cv2.destroyAllWindows()
