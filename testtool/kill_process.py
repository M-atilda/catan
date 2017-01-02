#! /usr/bin/python
#coding: utf-8
import sys
import os

def main():
    for line in open('./testtool/resource/ps.txt', 'r'):
        #print(line)
        if not line.find("node") == -1:
            p_id = line.split(' ')[0]
            if not os.system('kill ' + p_id) == 0:
                print("next target")
                p_id = line.split(' ')[1]
                os.system('kill ' + p_id)
            print(line)
            print('kill ' + p_id)
        if not line.find("python3") == -1:
            p_id = line.split(' ')[0]
            if not os.system('kill ' + p_id) == 0:
                p_id = line.split(' ')[1]
                os.system('kill ' + p_id)
            print(line)
            print('kill ' + p_id)

if __name__=='__main__':
    main()
