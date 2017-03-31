#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import glob
import cv2 as cv
import os.path
import fnmatch
import shutil
from operator import itemgetter, attrgetter

folder_path = "/home/lixihua/ali-datas/caltechPedestrians/data/images"
new_files = []

f = open(folder_path+"/files.txt", "w")

for root, dirs, files in os.walk(folder_path):
    for file in sorted(files):
        if file.find(".jpg") == -1: continue
        new_files.append(file.split(".")[0].split("_")[0:2] + [int(file.split(".")[0].split("_")[2])])

for file in sorted(sorted(sorted(new_files, key=itemgetter(2)), key=itemgetter(1)), key=itemgetter(0)):
    print file[0]+"_"+file[1]+"_"+str(file[2])+".jpg"
    f.write(folder_path+"/"+file[0]+"_"+file[1]+"_"+str(file[2])+".jpg")
    f.write("\n")

f.close()
