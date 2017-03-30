#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import json
import glob
import cv2 as cv
from collections import defaultdict

annotations = json.load(open('data/annotations.json'))

out_dir = 'data/plots'
if not os.path.exists(out_dir):
    os.makedirs(out_dir)

img_fns = defaultdict(dict)

for fn in sorted(glob.glob('data/images/*.jpg')):
    set_name = re.search('(set[0-9]+)', fn).groups()[0]
    img_fns[set_name] = defaultdict(dict)

for fn in sorted(glob.glob('data/images/*.jpg')):
    set_name = re.search('(set[0-9]+)', fn).groups()[0]
    video_name = re.search('(V[0-9]+)', fn).groups()[0]
    img_fns[set_name][video_name] = []

for fn in sorted(glob.glob('data/images/*.jpg')):
    set_name = re.search('(set[0-9]+)', fn).groups()[0]
    video_name = re.search('(V[0-9]+)', fn).groups()[0]
    n_frame = re.search('_([0-9]+)\.jpg', fn).groups()[0]
    img_fns[set_name][video_name].append((int(n_frame), fn))

cv.namedWindow("Video")
n_objects = 0
for set_name in sorted(img_fns.keys()):
    for video_name in sorted(img_fns[set_name].keys()):
        #wri = cv.VideoWriter(
        #    'data/plots/{}_{}.avi'.format(set_name, video_name),
        #    cv.VideoWriter_fourcc(*'XVID'), 30, (640, 480))
        for frame_i, fn in sorted(img_fns[set_name][video_name]):
            img = cv.imread(fn)
            if str(frame_i) in annotations[set_name][video_name]['frames']:
                data = annotations[set_name][
                    video_name]['frames'][str(frame_i)]
                for datum in data:
                    x, y, w, h = [int(v) for v in datum['pos']]
                    cv.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    n_objects += 1
                cv.imshow("Video", img)
                cv.waitKey(5)
                #wri.write(img)
        #wri.release()
        print(set_name, video_name)
print(n_objects)
