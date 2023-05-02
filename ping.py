from datetime import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

options = Options()
options.headless = True
profile = webdriver.FirefoxProfile(r"C:\Users\yop\AppData\Roaming\Mozilla\Firefox\Profiles\2l6nyyax.default-release")
service = Service(r'./drivers/geckodriver.exe')

root = 'https://carrieres-marbrume.herokuapp.com/'

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = 'Next ping in {:02d}:{:02d} minutes'.format(
            mins, secs)
        print(timeformat, end='\r')
        sleep(1)
        time_sec -= 1

def ping():

    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    try:
        driver = webdriver.Firefox(
            options=options, service=service)
        driver.get(root)
        sleep(2)
        driver.close()
        print(f'{date_time} : Ping Ok')
    except:
        driver.close()


if __name__ == '__main__':
    while True:
        ping()
        countdown(1800)