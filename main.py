# -*- coding: utf-8 -*-
"""
@author: Omen
@time: 2024/3/12 13:02
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from random import randint


# init driver
def load_driver(url: str):
    options = webdriver.ChromeOptions()
    options.add_argument('disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options=options)
    driver.get(url)  # url = 'https://www.wjx.cn/vm/Pza9Oiz.aspx# '
    sleep(2)
    return driver


# 获取所有题目
def get_all_questions(driver):
    return driver.find_elements(By.CSS_SELECTOR, '.fieldset>div.field.ui-field-contain')


# 单选题
def click_radio(driver):
    # 获取所有题目
    res = get_all_questions(driver)
    for i in res:
        i = i.find_elements(By.CSS_SELECTOR, '.ui-controlgroup.column1>div.ui-radio')
        i[randint(0, len(i) - 1)].click()
        # 调整点击间隔，默认0.5秒
        sleep(0.5)


# 提交
def submit(driver):
    driver.find_element(By.CSS_SELECTOR, '.submitbtn.mainBgColor').click()


def main():
    # 问卷地址
    url = '*****************'
    driver = load_driver(url)
    click_radio(driver)
    submit(driver)


if __name__ == '__main__':
    main()
