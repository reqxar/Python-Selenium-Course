from selenium import webdriver
import math, time

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

link = 'http://suninjuly.github.io/get_attribute.html'
browser = webdriver.Chrome()
browser.get(link)
x = browser.find_element_by_css_selector("#treasure").get_attribute("valuex")
x = calc(x)
browser.find_element_by_css_selector("#answer").send_keys(x)
browser.find_element_by_css_selector("#robotCheckbox").click()
browser.find_element_by_css_selector("#robotsRule").click()
browser.find_element_by_tag_name("button").click()
time.sleep(10)
browser.quit()
