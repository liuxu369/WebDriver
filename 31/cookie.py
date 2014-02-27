# -*- coding: utf-8 -*- 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

dr = webdriver.Chrome()

url = 'http://www.baidu.com'
dr.get(url)

print dr.get_cookies()
dr.delete_all_cookies()
dr.add_cookie({'name': 'BAIDUID', 'value': '0E09C60A19F8DFD50A9F6FF7B118023A:FG=1'})
dr.add_cookie({'name': 'BDUSS', 'value': 'mtsSlFmay10N1V6Z1hNSHVYNU14fi1TVk1uZmV4SVJaUFNId0lpRTAtNGw3elpUQVFBQUFBJCQAAAAAAAAAAAEAAADSUO0vwfq428'})

dr.get(url)

sleep(3)
# dr.quit()