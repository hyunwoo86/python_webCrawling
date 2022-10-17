# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import threading
import time

import requests
import csv
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By # https://wkdtjsgur100.github.io/selenium-xpath/
from selenium.webdriver.support.ui import WebDriverWait   # 해당 태그를 기다림 (https://neung0.tistory.com/m/40)
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException    # 태그가 없는 예외 처리

def Test():
    url = "https://naver.com"
    browser = webdriver.Safari()
    browser.get(url)
    print(browser.title)
    # 현재 창에서 스크린샷 찍고 저장
    browser.get_screenshot_as_file('./sample.png')

    # 입력창에 텍스트 입력
    browser.find_element(By.XPATH, '//*[@id="query"]').send_keys('selenium')

    # 특정 버튼 클릭
    browser.find_element(By.XPATH, '//*[@id="search_btn"]').click()

    try:
        element = WebDriverWait(browser, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "wrap-new.api_animation"))
            # browser.find_element(By.XPATH, '//body[@class="wrap-new api_animation"]')
        )  # 입력창이 뜰 때까지 대기
        # print(element)
    finally:
        pass

    # time.sleep(10)
    value = browser.find_element(By.XPATH, '//body[@class="wrap-new api_animation"]')
    print(value)

    # driver 종료
    browser.quit()



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    Test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
