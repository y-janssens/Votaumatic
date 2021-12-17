from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
from bs4 import BeautifulSoup
import requests

firefox_options = Options()
firefox_options.headless = True
fp = webdriver.FirefoxProfile(
    "C:/Users/scorp/AppData/Roaming/Mozilla/Firefox/Profiles/7khe95ju.default-release")

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument('headless')
chrome_options.add_argument('log-level=3') 

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

with open('log.txt', 'w', encoding='utf-8') as f:
    f.write('')

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
            driver = webdriver.Chrome(options=chrome_options)
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

def notification():
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    try:
        driver = webdriver.Firefox(firefox_profile=fp, options=firefox_options)
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
    else:
        driver.close()


while True:
    vote()
    notification()
    countdown(7500)