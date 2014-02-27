from selenium import webdriver
from time import sleep

dr = webdriver.Firefox()

dr.maximize_window()

sleep(3)

dr.close()