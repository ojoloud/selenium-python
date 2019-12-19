#!/usr/bin/env python
"""
Author: Olga Joloud
File: target_platform.py 
Purpose: classes to initialize driver per platform
"""
from enum import Enum
from dataclasses import dataclass
import sys
from selenium import webdriver
@dataclass
class TargetPlatform(Enum):
    CHROME=('chrome', 'webdriver.Chrome()')
    FIREFOX=('firefox','webdriver.Firefox()')
    ANY=('firefox','webdriver.Firefox()')

    def __init__(self, browser: str, driver: str):
        self.browser=browser
        self.driver=driver
    @property
    def get_browser(self):
        return self.browser
    @property
    def get_driver(self):
        return self.driver
@dataclass
class TargetPlatformMethods:
    def __init__(self):
        self.platform=TargetPlatform.ANY
    def get_platform(self, browser: str)->TargetPlatform:
        if browser is '':
            raise Exception ("browser value can not be null")
        for value in TargetPlatform:
            if value.get_browser==browser.strip().lower():
                self.platform=value
                break
        return self.platform
@dataclass
class Driver(object):
    def __init__(self, target: TargetPlatform):
        self.target=target
    def get_platform_driver(self):
        return self.target.get_driver
