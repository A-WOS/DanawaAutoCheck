import os
import requests
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome('D:/DanawaAutoCheck/src/chromedriver.exe')
browser.get('https://auth.danawa.com/login?url=http%3A%2F%2Fwww.danawa.com%2Fmember%2FmyPage.php')
browser.implicitly_wait(3)

browser.find_element(By.ID, "danawa-member-login-snsButton-kakao").click()
time.sleep(500)

print("login")
