from selenium.webdriver import Firefox
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from time import sleep

profile_path = r'C:\Users\scorp\AppData\Roaming\Mozilla\Firefox\Profiles\7khe95ju.default-release'
options=Options()
options.headless = False
options.set_preference('profile', profile_path)
service = Service(r'./drivers/geckodriver.exe')

driver = Firefox(service=service, options=options)

driver.get('https://marbrume.forumactif.com')

sleep(60)
driver.quit()