from selenium.webdriver.common.by import By
from selenium.webdriver.common.proxy import *
from selenium import webdriver
from time import sleep
import random

options_drive = webdriver.ChromeOptions()
options_drive.add_argument('log-level=3')
options_drive.add_argument('headless')
drive = webdriver.Chrome(options=options_drive)


def get_free_proxies(drive):
    drive.get('https://sslproxies.org')

    table = drive.find_element(By.TAG_NAME, 'table')
    thead = table.find_element(
        By.TAG_NAME, 'thead').find_elements(By.TAG_NAME, 'th')
    tbody = table.find_element(
        By.TAG_NAME, 'tbody').find_elements(By.TAG_NAME, 'tr')

    headers = []
    for th in thead:
        headers.append(th.text.strip())

    proxies = []
    for tr in tbody:
        proxy_data = {}
        tds = tr.find_elements(By.TAG_NAME, 'td')
        for i in range(len(headers)):
            proxy_data[headers[i]] = tds[i].text.strip()
        proxies.append(proxy_data)

    return proxies


free_proxies = get_free_proxies(drive)
prox = []

for i in free_proxies:
    if i['Country'] == 'France':
        free_ip = i['IP Address']
        free_port = i['Port']
        free_proxy = f'{free_ip}:{free_port}'
        prox.append(free_proxy)

proxy = prox[0]


root = 'http://www.root-top.com/topsite/'
topsites = [f'{root}virtu4lgames/in.php?ID=4969', f'{root}gilgamesh/in.php?ID=8372', f'{root}justmarried/in.php?ID=763',
            f'{root}melu/in.php?ID=4220', f'{root}pubrpgdesign/in.php?ID=2731', f'{root}niviel/in.php?ID=1194']


def vote():

    options = webdriver.ChromeOptions()
    options.add_argument('log-level=3')
    options.add_argument('--proxy-server=%s' % proxy)
    # options.add_argument('headless')
    try:
        driver = webdriver.Chrome(options=options)
        driver.get(topsites[1])
        sleep(2)
        driver.refresh()
        sleep(2)
        button = driver.find_element(By.ID, 'BA')
        button.click()
        sleep(200)
        # driver.close()
        print('Success')
    except:
        sleep(200)
        print('Error')


while True:
    vote()
    sleep(7500)
