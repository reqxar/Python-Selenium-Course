from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math, time, os

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))


link = 'http://suninjuly.github.io/explicit_wait2.html'
browser = webdriver.Chrome()
browser.get(link)
WebDriverWait(browser, 12).until(
    EC.text_to_be_present_in_element((By.ID, "price"), "$100")
)

browser.find_element_by_css_selector("#book").click()
x = calc(int(browser.find_element_by_css_selector("#input_value").text))
browser.find_element_by_css_selector("#answer").send_keys(x)
browser.find_element_by_css_selector("#solve").click()
time.sleep(10)



