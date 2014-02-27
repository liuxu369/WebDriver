from selenium import webdriver

f = webdriver.Firefox()
f.implicitly_wait(10) # seconds
f.get("http://somedomain/url_that_delays_loading")
myDynamicElement = f.find_element_by_id("myDynamicElement")
