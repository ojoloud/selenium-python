#!/usr/bin/env python
"""
Author: Olga Joloud
File: login_page.py
Purpose: implements login page
"""


from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base.target_platform
from base.target_platform import Driver
from base.page import Page
import sys
from selenium import webdriver
from dataclasses import dataclass
@dataclass
class LoginPage(Page):
    def __init__(self, driver: Driver):
        super().__init__(driver)
        #self.driver=driver
    def go_to_login(self, url: str):
        super().go_to(url)
    def sign_in(self, user: str, password: str):
        super().set_text(*LoginPageLocator.NAME_FIELD, user)
        super().click_button(*LoginPageLocator.NEXT_NAME_BUTTON)
        super().set_text(*LoginPageLocator.PASSWD_FIELD, password)
        super().click_button(*LoginPageLocator.NEXT_PASSWD_BUTTON)
class LoginPageLocator(object):
    NAME_FIELD = (By.NAME, 'identifier')
    NEXT_NAME_BUTTON = (By.XPATH, '//*[@id="identifierNext"]')
    PASSWD_FIELD = (By.NAME, 'password')
    NEXT_PASSWD_BUTTON = (By.XPATH, '//*[@id="passwordNext"]')
