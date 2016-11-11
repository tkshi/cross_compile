# -*- coding: utf-8 -*-

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import re
import platform

from Twitter import Twitter
OAUTH_SITE_URL = "http://36.55.241.31/twitter/admin/Share/login"
LOGIN_URL = "http://36.55.241.31/twitter/admin"
LOGIN_ID = "admin"
LOGIN_PASS = "123456"

TWITTER_ID = "vitalinakudrya3"
TWITTER_PASS = "cmkUZyJytm"
TWITTER_EMAIL = ""


class SocialLogin:
    def __init__(self,driver,app_ip):
        self.app_ip = app_ip
        self.LOGIN_URL = "http://{app_ip}/twitter/admin".format(app_ip=app_ip)
        self.OAUTH_SITE_URL = "http://{app_ip}/twitter/admin/Share/login".format(app_ip=app_ip)
        self.driver = driver
        self.driver.get(self.LOGIN_URL)
        elem = self.driver.find_element_by_css_selector('#AdminUsername')
        elem.send_keys(LOGIN_ID)
        elem = self.driver.find_element_by_css_selector('#AdminPassword')
        elem.send_keys(LOGIN_PASS)
        elem = self.driver.find_element_by_css_selector('#AdminAdminIndexForm > fieldset > input.btn.btn-lg.btn-success.btn-block')
        elem.click()

    def twitterLogin(self):
        self.driver.get(self.OAUTH_SITE_URL)
        elem = self.driver.find_element_by_css_selector('#allow')
        elem.click()
        sleep(5)

if __name__ == '__main__':
    try:
        driver = Twitter(twitter_id=TWITTER_ID,twitter_pass=TWITTER_PASS,twitter_email=TWITTER_EMAIL).getDriver()
    except Exception:
        driver = webdriver.Chrome()
    sl = SocialLogin(driver=driver,app_ip='36.55.241.31')
    sl.twitterLogin()
