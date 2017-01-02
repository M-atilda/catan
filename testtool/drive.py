#! /usr/bin/python
#coding: utf-8

import os
import time
import cv2

#XXX: select evaluate storategy
#import match_hist as m
import match_temp as m

#XXX: path from the dir makefile exists
g_image_path = './testtool/resource/temp.png'
g_threshold = 0.99

def compare(correct_img_path):
    global g_image_path
    screen_img = cv2.imread(g_image_path)

    #trimming area
    left = 350
    top = 140
    width = 100
    height = 40

    trimminged_screen_img = screen_img[top : top + height, left : left + width]

    res = m.getSimilarity(trimminged_screen_img, correct_img_path)

    if (res > g_threshold):
        return True
    else:
        return False

#TODO: find butten and push automatically
def enter_login_page():
    os.system("xte 'mousemove 770 250'")
    os.system("xte 'mouseclick 1'")

def login():
    #type username
    os.system("xte 'mousemove 600 290'")
    os.system("xte 'mouseclick 1'")

    os.system("xte 'keydown Shift_L'")
    os.system("xte 'key U'")
    os.system("xte 'key M'")
    os.system("xte 'key A'")
    os.system("xte 'keyup Shift_L'")

    os.system("xte 'key Tab'")

    os.system("sleep 1")

    #type passward
    os.system("xte 'key c'")
    os.system("xte 'key a'")
    os.system("xte 'key t'")
    os.system("xte 'key a'")
    os.system("xte 'key n'")
    os.system("xte 'key 3'")
    os.system("xte 'key 9'")

    os.system("sleep 1")

    os.system("xte 'key Tab'")
    os.system("xte 'key Return'")

def start_game():
    os.system("xte 'mousemove 520 320'")
    os.system("xte 'mouseclick 1'")

def main():
    global g_image_path
    os.system('xwd -silent -out ' + g_image_path)
    os.system("xte 'mouseclick 1'")
    error_counter = 0

    result = False

    #TODO: hard coding
    while not result:
        if compare('./testtool/resource/cut_toppage_new.png'):
            print("match with the top page")
            enter_login_page()
            time.sleep(1)
        elif compare('./testtool/resource/cut_login_new.png'):
            print("match with the login page")
            login()
            time.sleep(1)
        elif compare('./testtool/resource/cut_waitingroom_new.png'):
            print("match with the waiting room page")
            start_game()
            time.sleep(1)
        elif compare('./testtool/resource/cut_gameroom_new.png'):
            print("match with the game room page")
            result = True
        else:
            print("unknown page ...")
            error_counter += 1
            time.sleep(1)
            if error_counter >= 10:
                raise Exception("target not found ...")

        #update
        os.system('rm ./testtool/resource/temp.png')
        os.system('xwd -silent -out ' + g_image_path)
        os.system("xte 'mouseclick 1'")


if __name__ == '__main__':
    try:
        main()
        print("test success")
    except Exception as e:
        print(e)
        print("test failed")
