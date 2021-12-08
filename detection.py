import cv2 as cv
import easyocr
import numpy as np
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('log-level=3')


def read():

    url = 'http://www.root-top.com/topsite/obsession27/in.php?ID=23430'
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.refresh()
    driver.save_screenshot("img.png")
    #sleep(2)

    try:
        img = cv.imread('img.png')
        gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
        bfilter = cv.bilateralFilter(gray, 11, 17, 17)
        th2 = cv.adaptiveThreshold(bfilter, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                   cv.THRESH_BINARY, 99, 10)
        blank = np.zeros(img.shape[:2], dtype='uint8')
        mask = cv.rectangle(blank, (900, 335), (700, 200), (255, 255, 255), -1)
        masked = cv.bitwise_and(th2, th2, mask=mask)

        reader = easyocr.Reader(['en'], verbose=False)
        result = reader.readtext(masked, allowlist='0123456789')
        output = list(result[0][-2])
        if len(output) == 2:
            print(f'result: {output[0]}, {output[1]}')
            cases = driver.find_elements(By.CSS_SELECTOR, 'td.case')
            for i in range(0, 25):
                if cases[i].text == f'  {output[0]}  ':
                    cases[i].click()
                    sleep(1)

            for i in range(0, 25):
                if cases[i].text == f'  {output[1]}  ':
                    cases[i].click()
                    sleep(1)

            print('Success')
        else:
            print('Error')
    except:
        pass


while True:
    read()
    #sleep(7500)
