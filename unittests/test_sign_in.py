#!/usr/bin/env python

from unittest import TestCase
from pages.login_page import LoginPage
import  base.target_platform
from base.target_platform import Driver
from selenium import webdriver
class TestSignIn(TestCase):
    """
    Defines tests for Sign In
    
    """
    def test_setUp(self):
        target=base.target_platform.TargetPlatformMethods()
        driver_name=Driver(target.get_platform('chrome'))
        driver=eval(driver_name.get_platform_driver())
        login_page=LoginPage(driver)
        login_page.go_to_login('https://accounts.google.com/')
        login_page.sign_in('name','text')
