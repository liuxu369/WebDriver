from selenium import webdriver
from time import sleep

dr = webdriver.Firefox()

dr.set_window_size(240, 320)

sleep(3)

dr.get('http://www.3g.qq.com')

sleep(5)

dr.close()