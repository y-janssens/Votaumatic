import cv2 as cv
import easyocr
import numpy as np
import shutil
import os
import sys

""" for i in range(1, 101):
    if i < 10:
        os.mkdir(f'./dbtest/0{i}')
    else:
        os.mkdir(f'./dbtest/{i}') """


for i in range(1, 101):
    try:
        orig = rf'./dbtest/img{i}.png'
        img = cv.imread(f'./dbtest/img{i}.png')
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        bfilter = cv.bilateralFilter(gray, 11, 17, 17)
        th2 = cv.adaptiveThreshold(bfilter, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                   cv.THRESH_BINARY, 99, 10)

        reader = easyocr.Reader(['en'], verbose=False)
        result = reader.readtext(th2, allowlist='0123456789')
        output = list(result[0][-2])
        target = rf'./dbtest/{output[0]}{output[1]}'
        if len(output) == 2:
            print(f'result: {output[0]}, {output[1]}')
            print('Success')
            shutil.move(orig, target)
        else:
            print('Missread')
    except:
        print('Error')
