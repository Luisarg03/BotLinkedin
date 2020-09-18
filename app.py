import time
from modules.bot import login, search, filter, select
from modules.listtxt import txt
from config import config
from selenium import webdriver

config = config()
driver = webdriver.Chrome(config['driver'])
driver.maximize_window()

time.sleep(2)
login(driver, config['user'], config['password'])
time.sleep(2)
search(driver, config['word'])
time.sleep(2)
filter(driver)
time.sleep(2)
dic = select(driver)

txt(dic)
