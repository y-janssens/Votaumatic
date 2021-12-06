from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from bs4 import BeautifulSoup
import requests

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

options = webdriver.ChromeOptions()
options.add_argument(
    "user-data-dir=C:/Users/scorp/AppData/Local/Google/Chrome/User Data")
options.add_argument('--profile-directory=Profile 0')
options.add_argument('log-level=3')

def countdown(time_sec):
    while time_sec:
        mins, secs = divmod(time_sec, 60)
        timeformat = 'Next vote in {:02d}:{:02d} minutes'.format(
            mins, secs)
        print(timeformat, end='\r')
        sleep(1)
        time_sec -= 1

def notification():
    now = datetime.now()
    date_time = now.strftime("%d/%m/%Y %H:%M:%S")
    try:
        driver = webdriver.Chrome(chrome_options=options)
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
    except:
        print('error')

while True:
    notification()
    countdown(7500)
