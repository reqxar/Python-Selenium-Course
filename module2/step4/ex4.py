from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math, time, os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)
browser.find_element_by_id("button")
time.sleep(10)
browser.quit()