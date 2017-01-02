#! /usr/bin/python
import numpy as np
import cv2

def getSimilarity(img, correct_img_path):
    template_img = cv2.imread(correct_img_path)

    result = cv2.matchTemplate(img, template_img, cv2.TM_CCOEFF_NORMED)
    print(result)

    return result


#for debug
if __name__ == '__main__':
    img = cv2.imread('./resource/toppage_new.png')
    getSimilarity(img, './resource/waitingroom_new.png')
