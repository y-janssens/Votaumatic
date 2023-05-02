from datetime import datetime
from time import sleep
import requests
from bs4 import BeautifulSoup
from selenium.webdriver import Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.firefox.service import Service

profile_path = r'C:\Users\scorp\AppData\Roaming\Mozilla\Firefox\Profiles\z8959r85.default-release'
options = Options()
options.headless = True
service = Service(r'./drivers/geckodriver.exe')

root = 'http://www.root-top.com/topsite/'
topsites = [f'{root}virtu4lgames/in.php?ID=4969', f'{root}gilgamesh/in.php?ID=8372', f'{root}justmarried/in.php?ID=763',
            f'{root}melu/in.php?ID=4220', f'{root}pubrpgdesign/in.php?ID=2731', f'{root}niviel/in.php?ID=1194']

root_url = 'https://marbrume.forumactif.com'
topics_index = requests.get(
    'https://marbrume.forumactif.com/f66-aider-le-forum').text
soup_index = BeautifulSoup(topics_index, 'lxml')
lasts_topics = soup_index.find_all('a', class_='topictitle')
last_topic_list = []

for i in lasts_topics:
    topic = i['href']
    last_topic_list.append(topic)

last_topic = root_url + last_topic_list[1]

driver = Firefox(
    firefox_profile=profile_path, options=options, service=service)


def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = 'Next vote in {:02d}:{:02d} minutes'.format(
            mins, secs)
        print(timeformat, end='\r')
        sleep(1)
        time_sec -= 1


def vote():
    for i in range(len(topsites)):
        now = datetime.now()
        date_time = now.strftime("%d/%m/%Y %H:%M:%S")
        try:
            driver.get(topsites[i])
            sleep(2)
            driver.refresh()
            sleep(2)
            button = driver.find_element(By.ID, 'BA')
            button.click()
            sleep(2)
            print(f'{date_time} : {topsites[i]} : Ok')
        except:
            print(f'{date_time} : {topsites[i]} : Error')
    with open('log.txt', 'a', encoding='utf-8') as f:
        f.write('\n')


def notification():
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")

    try:
        sleep(2)
        driver.get(last_topic)
        sleep(2)
        inputElement = driver.find_element(
            By.CSS_SELECTOR, ".sceditor-container textarea")
        sleep(1)
        inputElement.click()
        inputElement.send_keys('+1')
        sleep(1)
        inputElement.send_keys(Keys.TAB, Keys.TAB, Keys.ENTER)
        sleep(5)
        print(f'{date_time} : Vote Successful')
        unwatch = driver.find_elements(By.CSS_SELECTOR, 'span.gensmall')
        links = list(unwatch)
        button = links[-7]
        button.click()
        sleep(5)
        print(f'{date_time} : Topic unwatched')
    except:
        print('error')


if __name__ == '__main__':
    while True:
        vote()
        notification()
        try:
            driver.close()
        except:
            pass
        countdown(7500)
