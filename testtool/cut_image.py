#! /usr/bin/python
import cv2

left = 350
top = 140
width = 100
height = 40


img = cv2.imread('./resource/login_new.png')
img = img[top:top+height, left:left+width]
cv2.imshow('sample', img)
cv2.waitKey(0)
cv2.imwrite('cut_login_new.png', img)
