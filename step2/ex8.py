from selenium import webdriver
from selenium.webdriver.support.ui import Select
import math, time, os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/file_input.html'
browser = webdriver.Chrome()
browser.get(link)
input_elems = browser.find_elements_by_css_selector('input[type="text"]')
for elem in input_elems:
    elem.send_keys("s")
current_dir = os.path.abspath(os.path.dirname(__file__))
file_path = os.path.join(current_dir, 'ex8.txt')
browser.find_element_by_css_selector("#file").send_keys(file_path)
browser.find_element_by_tag_name("button").click()
time.sleep(10)
browser.quit()