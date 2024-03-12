# -*- coding: utf-8 -*-
"""
@author: Omen
@time: 2024/3/12 13:02
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from random import randint, sample
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# init driver
def load_driver(url: str):
    options = webdriver.ChromeOptions()
    options.add_argument('disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options=options)
    driver.get(url)  # url = 'https://www.wjx.cn/vm/Pza9Oiz.aspx# '
    sleep(1)
    return driver


# 获取所有题目
def get_all_questions(driver):
    return driver.find_elements(By.CSS_SELECTOR, '.fieldset>div.field.ui-field-contain')


# 判断是否为单选
def is_radio(res):
    i = res.find_element(By.CSS_SELECTOR, '.ui-controlgroup.column1>div')
    if i.get_attribute('class') == 'ui-radio':
        return True
    return False


# 单选题
def click_radio(res):
        i = res.find_elements(By.CSS_SELECTOR, '.ui-controlgroup.column1>div.ui-radio')
        i[randint(0, len(i) - 1)].click()
        # 调整点击间隔，默认0.5秒
        sleep(0.5)


# 多选题
def click_checkbox(res):
        i = res.find_elements(By.CSS_SELECTOR, '.ui-controlgroup.column1>div.ui-checkbox')
        num1,num2 = sample(range(0, len(i)), 2)
        i[num1].click()
        sleep(0.2)
        i[num2].click()
        # 调整点击间隔，默认0.5秒
        sleep(0.5)


# 提交
def submit(driver):
    driver.find_element(By.CSS_SELECTOR, '.submitbtn.mainBgColor').click()
    sleep(5)


def main():
    # 问卷地址
    url = '*********'
    driver = load_driver(url)
    res = get_all_questions(driver)
    for i in res:
        if is_radio(i):
            click_radio(i)
        else:
            click_checkbox(i)
    submit(driver)


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
