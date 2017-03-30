#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
import cv2 as cv
import os.path
import fnmatch
import shutil


def save_img(dname, fn, i, frame):
    cv.imwrite('{}/{}_{}_{}.png'.format(
        out_dir, os.path.basename(dname),
        os.path.basename(fn).split('.')[0], i), frame)

def open_save(filename, savepath, fn):
    f = open(filename, 'rb')
    string = str(f.read())
    splitstring = "\xFF\xD8\xFF\xE0\x00\x10\x4A\x46\x49\x46"
    strlist = string.split(splitstring)
    f.close()
    count = 0
    fn_s = fn.split("/")
    #if os.path.exists(savepath): shutil.rmtree(savepath)
    #if not os.path.exists(savepath): os.mkdir(savepath)
    for img in strlist:
        filename = fn_s[-2]+"_"+fn_s[-1].split(".")[0]+"_"+str(count)+'.jpg'
        filenamewithpath = os.path.join(savepath, filename)
        #print filenamewithpath
        if count > 0:
            i = open(filenamewithpath, 'wb+')
            i.write(splitstring)
            i.write(img)
            i.close()
        count += 1

out_dir = 'data/images'
if not os.path.exists(out_dir):
    os.makedirs(out_dir)
for dname in sorted(glob.glob('data/set*')):
    for fn in sorted(glob.glob('{}/*.seq'.format(dname))):
        #cap = cv.VideoCapture(fn)
        #i = 0
        #while True:
        #    ret, frame = cap.read()
        #    if not ret:
        #        break
        #    save_img(dname, fn, i, frame)
        #    i += 1
        print(fn)
        open_save(fn, out_dir, fn)
