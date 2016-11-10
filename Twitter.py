# -*- coding: utf-8 -*-
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from time import sleep
from Error import *
import platform

TWITTER_ID = "rogovaevseviya1"
TWITTER_PASS = "HxC7pICH1w"
TWITTER_EMAIL = "RogovaEvseviya95@bk.ru"


# TWITTER_ID = "denisovafloren9"
# TWITTER_PASS = "sJjwfQwRa6"
# TWITTER_EMAIL = "DenisovaFlorensa1983@mail.ru"

class Twitter:
    def __init__(self,twitter_id,twitter_pass,twitter_email):
        self.twitter_id = twitter_id
        self.twitter_pass = twitter_pass
        self.twitter_email = twitter_email
        if  platform.system() == 'Windows':
            CHROMEDRIVER_PATH = "./chromedriver.exe"
        else:
            CHROMEDRIVER_PATH = "./chromedriver"
        self.driver = webdriver.Chrome(CHROMEDRIVER_PATH)
        self.success_login = False

        self.driver.get("https://twitter.com/login")
        elem = self.driver.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(2) > input')
        elem.send_keys(self.twitter_id)
        elem = self.driver.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > fieldset > div:nth-child(3) > input')
        elem.send_keys(self.twitter_pass)
        elem = self.driver.find_element_by_css_selector('#page-container > div > div.signin-wrapper > form > div.clearfix > button')
        elem.click()

        try:
            elem = self.driver.find_element_by_css_selector('#challenge_response')
            elem.send_keys(self.twitter_email)
            elem = self.driver.find_element_by_css_selector('#email_challenge_submit')
            elem.click()
        except NoSuchElementException as e:
            pass
        try:
            elem = self.driver.find_element_by_css_selector('#tweet-box-home-timeline')
            self.success_login = True
        except NoSuchElementException as e:
            self.driver.close()
            raise TwitterLoginError()
            self.success_login = False
        try:
            elem = self.driver.find_element_by_css_selector('#banners > div > div > div > button')
            self.driver.close()
            raise TwitterLoginError()
        except NoSuchElementException as e:
            pass
        try:
            elem = self.driver.find_element_by_css_selector('#page-container > div.BannersContainer > div > div > div:nth-child(2) > button')
            self.driver.close()
            raise TwitterLoginError()
        except NoSuchElementException as e:
            pass

    def getLoginStatus(self):
        return self.success_login

    def getDriver(self):
        return self.driver

    def setLangage(self):
        # page2
        self.driver.get('https://twitter.com/settings/account')
        if self.driver.title == u"Twitter / 設定":
            return True

        elem = self.driver.find_element_by_css_selector('#user_lang')
        elem.click()
        elem.find_element_by_css_selector("option[value='ja']").click()
        sleep(1)
        self.driver.find_element_by_css_selector('#settings_save').click()
        sleep(1)

        # page3
        elem = self.driver.find_element_by_css_selector('#auth_password')
        elem.send_keys(self.twitter_pass)
        elem = self.driver.find_element_by_css_selector('#save_password')
        elem.click()


    def setPhone(self,phone_number="0000"):
        self.driver.get('https://twitter.com/settings/add_phone')
        try:
            elem = self.driver.find_element_by_css_selector('#sms-phone-delete-form > div > h3')
            raise AlreadyAddedPhoneNumber
        except NoSuchElementException as e:
            pass
        try:
            elem = self.driver.find_element_by_css_selector('#cancel_registration')
            elem.click()
        except Exception:
            pass
        elem = self.driver.find_element_by_css_selector('#page-container > div.content-main > div.content-inner.no-stream-end > h3')
        elem = self.driver.find_element_by_css_selector('#device_country_code > option:nth-child(8)')
        elem.click()
        elem = self.driver.find_element_by_css_selector('#phone_number')
        elem.send_keys(phone_number)
        elem = self.driver.find_element_by_css_selector('#device_register')
        elem.click()
        try:
            elem = self.driver.find_element_by_css_selector('#settings-alert-box > h4')
            if(elem.text == u'試行回数の制限を超えました。しばらくしてからもう一度お試しください。'):
                self.close()
                raise CannotRegisterYetError
            self.close()
            raise PhoneNumberInvalidError
        except NoSuchElementException:
            pass
        return True
    def close(self):
        self.driver.close()

    def setPINKey(self,pin_code):
        self.driver.get('https://twitter.com/settings/add_phone')
        elem = self.driver.find_element_by_css_selector('#numeric_pin_raw')
        elem.send_keys(pin_code)
        elem = self.driver.find_element_by_css_selector('#device_verify')
        elem.click()
if __name__ == '__main__':
    try:
        tw = Twitter(twitter_id=TWITTER_ID,twitter_pass=TWITTER_PASS,twitter_email=TWITTER_EMAIL)
    except Exception:
        print('error')
    # print(tw.getLoginStatus())
    # tw.setLangage()
    # print(tw.setPhone(phone_number="(843) 471-0879"))
