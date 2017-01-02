#! /usr/bin/python
import numpy as np
import cv2

#XXX: not using template match, just compareing histgram

def getSimilarity(img, correct_img):
    template = cv2.imread(correct_img)

    img_hist = cv2.calcHist([img], [0], None, [256], [0, 256])
    temp_hist = cv2.calcHist([template], [0], None, [256], [0, 256])

    histval = cv2.compareHist(img_hist, temp_hist, 0)
    print(histval)
    return histval
