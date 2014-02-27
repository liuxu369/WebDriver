from selenium import webdriver
from time import sleep

dr = webdriver.Firefox()

url1 = 'http://www.baidu.com'
url2 = 'http://www.google.cn.hk'

dr.get(url1)

sleep(3)

dr.get(url2)


dr.back()
print 'the first url is %s' %(url1)

sleep(3)
dr.forward()
print 'the forward url is %s' %(url2)

sleep(3)

dr.quit()