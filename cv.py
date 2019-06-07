## Load an image

import cv2

import numpy as np

'''img = cv2.imread('cv2test.png',cv2.IMREAD_GRAYSCALE)
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.DestroyAllWindows()

'''

# Get pixel values

'''
img=cv2.imread('cv2test.png')
px=img[100,100]
print (px)

'''

img=cv2.imread('cv2test.png')
'''img[100,100]=[34,55,88]

cv2.imshow('image',img)
cv2.waitKey(23)
cv2.DestroyAllWindows()
'''

## Image shape (_,_,3) 3 tells colorea image
'''
print(img.shape)

#(800, 1920, 3)

# image size tells no of pixels
print(img.size)

#4608000

#Image type 
print(img.dtype)
#uint8
'''
# Region of Interest or cropping
roi=img[10:120,20:160]
cv2.imshow('image',roi)
cv2.waitKey()
cv2.DestroyAllWindows(0)
