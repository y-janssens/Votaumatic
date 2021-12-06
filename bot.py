from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime
from time import sleep

options = webdriver.ChromeOptions()
options.add_argument('headless')
options.add_argument('log-level=3')

root = 'http://www.root-top.com/topsite/'
topsites = [f'{root}virtu4lgames/in.php?ID=4969', f'{root}gilgamesh/in.php?ID=8372', f'{root}justmarried/in.php?ID=763',
            f'{root}melu/in.php?ID=4220', f'{root}pubrpgdesign/in.php?ID=2731', f'{root}niviel/in.php?ID=1194']

with open('log.txt', 'w', encoding='utf-8') as f:
    f.write('')


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = 'Next vote session in {:02d}:{:02d} minutes'.format(
            mins, secs)
        print(timeformat, end='\r')
        sleep(1)
        time_sec -= 1


def vote():
    for i in range(len(topsites)):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")
        try:
            driver = webdriver.Chrome(options=options)
            driver.get(topsites[i])
            sleep(2)
            driver.refresh()
            sleep(2)
            button = driver.find_element(By.ID,'BA')
            button.click()
            sleep(2)
            driver.close()
            with open('log.txt', 'a', encoding='utf-8') as f:
                f.write(f'{date_time} : {topsites[i]} : Ok \n')
            print(f'{date_time} : {topsites[i]} : Ok')
        except:
            with open('log.txt', 'a', encoding='utf-8') as f:
                f.write(f'{date_time} : {topsites[i]} : Error \n')
            print(f'{date_time} : {topsites[i]} : Error')
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write('\n')


while True:
    vote()
    countdown(7500)
