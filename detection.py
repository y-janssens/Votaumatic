import cv2 as cv
import easyocr
import requests
import shutil
from requests.api import request
from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime
from time import sleep
from bs4 import BeautifulSoup

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('log-level=3')

""" url = 'http://www.root-top.com/topsite/obsession27/in.php?ID=23430'

driver = webdriver.Chrome(options=options)
driver.get(url)
sleep(0.5)
driver.refresh()
sleep(0.5)
button = driver.find_elements(By.CSS_SELECTOR, 'td.case')
buttons = list(button)
for case in buttons:
    result = case.text
    if i in result:
        print(result) """


def read():
    global output
    root = 'https://www.root-top.com/include/captcha_vote/captcha.php?1638718615.png'
    r = requests.get(root, stream=True)
    if r.status_code == 200:
        with open("img.jpg", 'wb') as f:
            r.raw.decode_content = True
            shutil.copyfileobj(r.raw, f)
    try:
        img = cv.imread('img.jpg')
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        bfilter = cv.bilateralFilter(gray, 11, 17, 17)
        th2 = cv.adaptiveThreshold(bfilter, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                   cv.THRESH_BINARY, 99, 10)
        cv.imshow("test", th2)

        reader = easyocr.Reader(['en'], verbose=False)
        result = reader.readtext(th2, allowlist='0123456789')
        output = list(result[0][-2])
        if len(output) == 2:
            print(f'result: {output[0]}, {output[1]}')
            cv.waitKey(0)
        else:
            pass
    except:
        pass


while True:
    read()
