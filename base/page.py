#!/usr/bin/env python
"""
Author: Olga Joloud
File: page.py 
Purpose: basic page template 
"""

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import base.target_platform
from base.target_platform import Driver
import sys
from selenium import webdriver
from dataclasses import dataclass
@dataclass
class Page(object):
        driver: Driver
        def __init__(self,driver: Driver):
            self.driver=driver
        def set_text(self, by: By, value: str, text: str):
            text_element=WebDriverWait(self.driver, 60).until(EC.presence_of_element_located((by, value)))
            text_element.clear()
            text_element.send_keys(text)
        def click_button(self, by: By, value: str):
        #Wait if the element clickable
            try: 
                button_element=WebDriverWait(self.driver, 60).until(EC.element_to_be_clickable((by, value)))
            except AttributeError as err:
                print ('Attribute not defined {}'.format(err))
            button_element.click()
        def go_to(self,url):
            self.driver.get(url)
    
