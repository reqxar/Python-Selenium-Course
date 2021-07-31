from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import math, time, pytest, unittest

def answer():
    return str(math.log(int(time.time())))

@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()
class TestMainPage1():
    message = ''
    links = [
        'https://stepik.org/lesson/236895/step/1',
        'https://stepik.org/lesson/236896/step/1',
        'https://stepik.org/lesson/236897/step/1',
        'https://stepik.org/lesson/236898/step/1',
        'https://stepik.org/lesson/236899/step/1',
        'https://stepik.org/lesson/236903/step/1',
        'https://stepik.org/lesson/236904/step/1',
        'https://stepik.org/lesson/236905/step/1'
        ]

    @pytest.mark.parametrize('links', links)
    def test_search(self, browser, links):
        link = links
        browser.get(link)
        textarea = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.TAG_NAME, "textarea"))
        )
        textarea.send_keys(answer())


        button = WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, ".submit-submission"))
        )
        button.click()
        test_answer = WebDriverWait(browser, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "pre[class='smart-hints__hint']"))
        )
        test_answer = test_answer.text
        if test_answer !="Correct!":
            self.message += test_answer
            print(self.message)
        assert test_answer == False

if __name__ == "__main__":
    unittest.main()    
        



        
