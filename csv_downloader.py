import time
from selenium import webdriver

USERNAME = 'castorx9000' # Your username
PASSWORD = '' # Your password
CHROMEDRIVER_PATH = 'https://drive.google.com/drive/folders/1bbmHHNee60j7ZHEBagd0eXtomRIWmvIC' # Insert the path of chromedriver (to be downloaded from "https://sites.google.com/a/chromium.org/chromedriver/downloads")

driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH)  

driver.get('https://footystats.org/login');


time.sleep(5) # Let the user actually see something!


search_box = driver.find_element_by_name('username')
search_box.send_keys(USERNAME)
search_box = driver.find_element_by_name('password')

search_box.send_keys(PASSWORD)



driver.find_element_by_id('register_account').submit()

time.sleep(5) # Let the user actually see something!


driver.get('https://footystats.org/c-dl.php?type=league&comp=298');  # Sample download 1
driver.get('https://footystats.org/c-dl.php?type=teams&comp=298');  # Sample download 2

time.sleep(5)


driver.quit()