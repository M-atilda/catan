#! /usr/bin/python
#coding: utf-8
import sys
import os

def main():
    for line in open('./testtool/resource/jobs.txt', 'r'):
        if not line.find("node") is -1:
            job_id = line.split(' ')[0]
            os.system('kill %' + job_id)
        if not line.find("python3") is -1:
            job_id = line.split(' ')[0]
            os.system('kill %' + job_id)

if __name__=='__main__':
    main()
