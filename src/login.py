from dotenv import load_dotenv
import os
from selenium.webdriver.common.by import By
import time

from set_chrome_driver import set_chrome_driver

browser = set_chrome_driver()
browser.get('https://auth.danawa.com/login?url=http%3A%2F%2Fwww.danawa.com%2Fmember%2FmyPage.php')
browser.implicitly_wait(3)

browser.find_element(By.ID, "danawa-member-login-snsButton-kakao").click()

browser.switch_to.window(browser.window_handles[-1])

browser.get(browser.current_url)

load_dotenv()

KAKAO_ID = os.environ.get("EMAIL")
KAKAO_PW = os.environ.get("PW")

kakao_id = browser.find_element(By.ID, "loginKey--1")
kakao_pw = browser.find_element(By.ID, "password--2")

kakao_id.send_keys(KAKAO_ID)
kakao_pw.send_keys(KAKAO_PW)

time.sleep(500)

print("login")
