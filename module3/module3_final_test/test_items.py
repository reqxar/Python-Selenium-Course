from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/."

def test_should_contain_button(browser):
    browser.get(link)
    button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".btn.btn-lg.btn-primary"))
        )

    assert button.text != 'Добавить в корзину', 'Такой кнопки нет'
