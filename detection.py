import cv2 as cv
import easyocr
import numpy as np
from selenium.webdriver.common.by import By
from selenium import webdriver
from time import sleep
from datetime import datetime

options = webdriver.ChromeOptions()
options.add_argument('log-level=3')
url = 'http://www.root-top.com/topsite/obsession27/in.php?ID=23430'
driver = webdriver.Chrome(options=options)


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = 'Next vote in {:02d}:{:02d} minutes'.format(
            mins, secs)
        print(timeformat, end='\r')
        sleep(1)
        time_sec -= 1


def read():
    driver.get(url)
    driver.refresh()
    driver.save_screenshot("img.png")
    success = False
    while success == False:
        try:
            img = cv.imread('img.png')
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
            bfilter = cv.bilateralFilter(gray, 11, 17, 17)
            th2 = cv.adaptiveThreshold(bfilter, 255, cv.ADAPTIVE_THRESH_MEAN_C,
                                       cv.THRESH_BINARY, 99, 10)
            blank = np.zeros(img.shape[:2], dtype='uint8')
            mask = cv.rectangle(blank, (900, 335),
                                (700, 200), (255, 255, 255), -1)
            masked = cv.bitwise_and(th2, th2, mask=mask)

            reader = easyocr.Reader(['en'], verbose=False)
            result = reader.readtext(masked, allowlist='123456789')
            output = list(result[0][-2])
            if len(output) == 2:
                print(f'result: {output[0]}, {output[1]}')
                cases = driver.find_elements(By.CSS_SELECTOR, 'td.case')
                for i in range(0, 25):
                    if cases[i].text == f'  {output[0]}  ':
                        cases[i].click()

                for i in range(0, 25):
                    if cases[i].text == f'  {output[1]}  ':
                        cases[i].click()

                print('Success')
                success = True
                break
            else:
                if success == True:
                    break
                else:
                    read()
                pass
        except:
            if success == True:
                break


def check():
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    driver.get(url)
    driver.refresh()
    try:
        verif = driver.find_element(
            By.XPATH, '//p[contains(text(), "' + '120 minutes' + '")]')
        print(f'{date_time} : Vote Successful')
        driver.close()
        pass
    except:
        print('Error')
        read()


""" def vote():
    read()
    try:
        check()
    except:
        read() """


while True:
    read()
    countdown(7500)
