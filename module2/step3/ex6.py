from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math, time, os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/redirect_accept.html'
browser = webdriver.Chrome()
browser.get(link)
browser.find_element_by_tag_name("button").click()
new_window = browser.window_handles[1]
browser.switch_to.window(new_window)
x = calc(int(browser.find_element_by_css_selector("#input_value").text))
browser.find_element_by_css_selector("#answer").send_keys(x)
browser.find_element_by_tag_name("button").click()
time.sleep(30)

