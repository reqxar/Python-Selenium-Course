from selenium import webdriver
import math
import time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/math.html'
browser = webdriver.Chrome()
browser.get(link)
x = browser.find_element_by_css_selector('#input_value').text
x = calc(x)

input1 = browser.find_element_by_css_selector("#answer")
input1.send_keys(x)
browser.find_element_by_css_selector("[for='robotCheckbox']").click()
browser.find_element_by_css_selector("[for='robotsRule']").click()
browser.find_element_by_tag_name('button').click()
time.sleep(30)
browser.quit()


