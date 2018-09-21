#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

# # 使Chrome不弹出界面，实现无界面爬取
chrome_options = Options()
chrome_options.add_argument('--headless')
chrome_options.add_argument('--disable-gpu')
browser = webdriver.Chrome(chrome_options=chrome_options)
# browser = webdriver.Chrome()


browser.get("https://www.evolution.land/")
time.sleep(3)
registerLink = browser.find_element_by_xpath('//*[@id="root"]/div/div[1]/div/div[2]/a[6]')
registerLink.click()
time.sleep(3)
qrCode = browser.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/div/div/div/div[1]')
print qrCode.value_of_css_property("width")
print qrCode.value_of_css_property("height")
browser.close()
browser.quit()

if __name__ == '__main__':
    pass
