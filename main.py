import os
import sys
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

    print(f'OS Platform: {sys.platform}')
    dirname = os.path.abspath(sys.argv[0])
    dirname = os.path.dirname(dirname)

    def exists(path):
        return os.path.exists(path)

    chrome_driver_path = os.path.join(dirname, 'chromedriver')
    firefox_driver_path = os.path.join(dirname, 'geckodriver')

    driver = None
    if os.path.exists(chrome_driver_path):
        driver = Chrome(chrome_driver_path)
    elif os.path.exists(firefox_driver_path):
        driver = Firefox(executable_path=firefox_driver_path)

    if driver is None:
        sys.stderr.write('No webdriver found.\n')
        exit(1)

    first = True
    driver.maximize_window()
    driver.implicitly_wait(1)
    click = lambda e: driver.execute_script("arguments[0].click();", e)
    try:
        for i, d in enumerate(data):
            print(f'{i + 1}/{len(data)} {d[0]} => {d[1]}')
            if d[3].lower() == 'ok':
                continue
            try:
                driver.get(url % d[0])
                if first:
                    click(driver.find_element_by_class_name('tlid-dismiss-button'))
                click(driver.find_element_by_class_name('tlid-send-feedback-link'))
                time.sleep(1)
                n = len(driver.find_elements_by_tag_name('iframe'))
                for i in reversed(range(n)):
                    driver.switch_to.frame(i)
                    e = driver.find_elements_by_tag_name('textarea')
                    if len(e) == 1:
                        e[0].send_keys(template % d[1])
                        click(driver.find_element_by_xpath('//input[@type="checkbox"]'))
                        click(driver.find_element_by_xpath('//button[@type="submit"]'))
                        driver.switch_to.default_content()
                        break
                    driver.switch_to.default_content()

                time.sleep(1)
                driver.find_element_by_class_name('tlid-suggest-edit-button').click()
                driver.find_element_by_class_name('contribute-target').clear()
                driver.find_element_by_class_name('contribute-target').send_keys(d[1])
                driver.find_element_by_class_name('jfk-button-action').click()
                first = False
            except Exception as e:
                sys.stderr.write(f'Error, {e}\nSkip!\n')
    finally:
        driver.quit()

    print('Done!')

def get_sheet():
    content = requests.get('http://gtig.ddns.net/').content
    return json.loads(content)

if __name__ == "__main__":
    main()
