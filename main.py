import os
import pickle
import time
import json
import requests

from selenium.webdriver import Chrome, Firefox
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


def main():
    template = 'This translation is culturally inappropriate. The correct translation should be %s. I selected Traditional Chinese, which should translate into phrases used in Taiwan, but it gave me phrases used in China (Simplified Chinese).'
    url = 'https://translate.google.com/#view=home&op=translate&sl=auto&tl=zh-TW&text=%s'
    data = get_sheet()

    if os.path.exists('./chromedriver.exe'):
        driver = Chrome()
    else:
        driver = Firefox()
    driver.maximize_window()
    driver.implicitly_wait(1)
    first = True
    try:
        for d in data:
            if d[3].lower() == 'ok':
                continue
            driver.get(url % d[0])
            if first:
                driver.find_element_by_class_name('tlid-dismiss-button').click()
            element = driver.find_element_by_class_name('tlid-send-feedback-link')
            driver.execute_script("arguments[0].click();", element)
            time.sleep(1)
            n = len(driver.find_elements_by_tag_name('iframe'))
            print(f'{n} iframe found')
            for i in reversed(range(n)):
                driver.switch_to.frame(i)
                e = driver.find_elements_by_tag_name('textarea')
                if len(e) == 1:
                    e[0].send_keys(template % d[1])
                    driver.find_element_by_xpath('//input[@type="checkbox"]').click()
                    driver.find_element_by_xpath('//button[@type="submit"]').click()
                    driver.switch_to.default_content()
                    print(f'Feedback submit')
                    break
                driver.switch_to.default_content()

            time.sleep(1)
            driver.find_element_by_class_name('tlid-suggest-edit-button').click()
            driver.find_element_by_class_name('contribute-target').clear()
            driver.find_element_by_class_name('contribute-target').send_keys(d[1])
            driver.find_element_by_class_name('jfk-button-action').click()
            print(f'Suggestion submit')
            first = False
    finally:
        driver.quit()

    print('Done!')

def get_sheet():
    return json.loads(requests.get('http://nlp4.cse.ntou.edu.tw:8080/').content)

if __name__ == "__main__":
    main()
