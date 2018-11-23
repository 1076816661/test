
# coding=utf-8
from selenium import webdriver
import time
browser = webdriver.Chrome(executable_path='C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe')
browser.get('https://www.baidu.com')
input = browser.find_element_by_id('kw')#找到搜索框
input.send_keys('白玉婷')#传送入关键词
time.sleep(2)
input.clear()#清空搜索框
input.send_keys('白玉川')
input.send_keys('白玉川1')
input.send_keys('白玉川2')
button = browser.find_element_by_id('su')#找到搜索按钮
button.click()
time.sleep(5)
browser.close()

