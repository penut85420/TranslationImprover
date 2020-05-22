import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def main():
    template = 'This translation is culturally inappropriate. The correct translation should be %s. I selected Traditional Chinese, which should translate into phrases used in Taiwan, but it gave me phrases used in China (Simplified Chinese).'
    data = load_links('./link.txt')
    driver = Chrome('./chromedriver.exe')
    driver.maximize_window()
    driver.implicitly_wait(1)
    first = True
    try:
        for d in data:
            if d[3].lower() == 'ok':
                continue
            driver.get(d[4])
            if first:
                driver.find_element_by_class_name('tlid-dismiss-button').click()
            driver.find_element_by_class_name('tlid-send-feedback-link').click()
            n = len(driver.find_elements_by_tag_name('iframe'))
            for i in reversed(range(n)):
                driver.switch_to.frame(i)
                e = driver.find_elements_by_tag_name('textarea')
                if len(e) == 1:
                    e[0].send_keys(template % d[1])
                    driver.find_element_by_xpath('//input[@type="checkbox"]').click()
                    driver.find_element_by_xpath('//button[@type="submit"]').click()
                    driver.switch_to.parent_frame()
                    break
                driver.switch_to.parent_frame()
            time.sleep(1)
            # driver.find_element_by_xpath('//button[@type="button"]').click()
            driver.find_element_by_class_name('tlid-suggest-edit-button').click()
            driver.find_element_by_class_name('contribute-target').clear()
            driver.find_element_by_class_name('contribute-target').send_keys(d[1])
            driver.find_element_by_class_name('jfk-button-action').click()
            first = False
    finally:
        driver.quit()

def load_links(path):
    with open(path, 'r', encoding='UTF-8') as f:
        return [line.strip().split('\t') for line in f]

if __name__ == "__main__":
    main()
