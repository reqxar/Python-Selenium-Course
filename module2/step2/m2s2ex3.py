from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math, time


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/selects1.html'
browser = webdriver.Chrome()
browser.get(link)
sum = int(browser.find_element_by_css_selector("#num1").text) + int(browser.find_element_by_css_selector("#num2").text)
select = Select(browser.find_element_by_tag_name("select"))
select.select_by_value(str(sum))
browser.find_element_by_tag_name("button").click()
time.sleep(10)
browser.quit()