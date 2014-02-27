#coding:utf-8
from selenium import webdriver
import os
dr = webdriver.Chrome()

file_path = 'file:///' + os.path.abspath('breadcrumb.html')

dr.get(file_path)

#获得其父层级
anstors = dr.find_element_by_class_name('breadcrumb').find_elements_by_tagname('a')
#?????

sleep(1)


print dr.find_element_by_class_name('breadcrumb').find_element_by_class_name('active').text

dr.quit()