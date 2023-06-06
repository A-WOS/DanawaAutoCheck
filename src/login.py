import os
from selenium.webdriver.common.by import By
import time

from set_chrome_driver import set_chrome_driver

browser = set_chrome_driver()
browser.get('https://auth.danawa.com/login?url=http%3A%2F%2Fwww.danawa.com%2Fmember%2FmyPage.php')
browser.implicitly_wait(3)

browser.find_element(By.ID, "danawa-member-login-snsButton-kakao").click()

browser.switch_to.window(browser.window_handles[-1])

print("login")
