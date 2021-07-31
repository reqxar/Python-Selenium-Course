from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math, time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/execute_script.html'
browser = webdriver.Chrome()
browser.get(link)
x = int(browser.find_element_by_css_selector("#input_value").text)
x = calc(x)
button = browser.find_element_by_tag_name("button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
browser.find_element_by_css_selector("#answer").send_keys(x)
browser.find_element_by_css_selector("#robotCheckbox").click()
robots = browser.find_element_by_css_selector("#robotsRule")
browser.execute_script("return arguments[0].scrollIntoView(true);", robots)
robots.click()
button.click()
time.sleep(10)
browser.quit()