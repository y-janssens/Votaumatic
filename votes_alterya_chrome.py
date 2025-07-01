from selenium.webdriver.common.by import By
from selenium import webdriver
from datetime import datetime
from time import sleep


ROOT = 'http://www.root-top.com/topsite'

TOPSITES = [
    f'{ROOT}/virtu4lgames/in.php?ID=6916',
    f'{ROOT}/obsession27/in.php?ID=27483',
    f'{ROOT}/gilgamesh/in.php?ID=8668',
    f'{ROOT}/justmarried/in.php?ID=1247',
    f'{ROOT}/melu/in.php?ID=5321',
    f'{ROOT}/pubrpgdesign/in.php?ID=3471'
]


class AutoVote:
    def __init__(self):
        self.options = self.get_options()

    def get_options(self):
        options = webdriver.ChromeOptions()
        options.add_argument('log-level=3')
        options.add_argument('headless')
        return options

    def countdown(self, delay):
        while delay:
            mins, secs = divmod(delay, 60)
            timeformat = 'Prochain vote dans {:02d}:{:02d} minutes'.format(
                mins, secs)
            print(timeformat, end='\r')
            sleep(1)
            delay -= 1

    def vote(self):
        driver = webdriver.Chrome(options=self.options)
        for topsite in TOPSITES:
            now = datetime.now()
            date_time = now.strftime("%d/%m/%Y %H:%M:%S")
            try:
                driver.get(topsite)
                sleep(2)
                driver.refresh()
                sleep(2)
                button = driver.find_element(By.ID, 'BA')
                button.click()
                sleep(2)
                print(f'{date_time} : {topsite} : Ok')
            except Exception as e:
                print(f'{date_time} : {topsite} : Erreur {e}')
        driver.quit()

    def session(self):
        self.vote()
        self.countdown(7500)


if __name__ == "__main__":
    voter = AutoVote()
    while True:
        voter.session()
