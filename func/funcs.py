# -*- coding: utf-8 -*-
"""
@author: Omen
@time: 2024/3/13 10:06
"""
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
from random import randint, sample, uniform
from func.ai import chat

# init driver
def load_driver(url: str):
    options = webdriver.ChromeOptions()
    options.add_argument('disable-blink-features=AutomationControlled')
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    sleep(1)
    return driver


# 获取所有题目
def get_all_questions(driver):
    return driver.find_elements(By.CSS_SELECTOR, '.fieldset>div.field.ui-field-contain')


# 判断题型
def is_radio(res):
    if res.get_attribute('type') == '2':
        return 'textarea'
    elif res.get_attribute('type') == '3':
        return 'radio'
    elif res.get_attribute('type') == '4':
        return 'checkbox'
    else:
        return False


# 获取简答题问题
def get_textarea_question(res):
    res = res.find_element(By.CSS_SELECTOR, '.field-label>div.topichtml')
    return res.text


# 单选题
def click_radio(res):
    i = res.find_elements(By.CSS_SELECTOR, '.ui-controlgroup.column1>div.ui-radio')
    i[randint(0, len(i) - 1)].click()
    # 调整点击间隔
    sleep(round(uniform(0.4, 0.6), 2))


# 多选题
def click_checkbox(res):
    i = res.find_elements(By.CSS_SELECTOR, '.ui-controlgroup.column1>div.ui-checkbox')
    num1, num2 = sample(range(0, len(i)), 2)
    i[num1].click()
    sleep(round(uniform(0.20, 0.25), 2))
    i[num2].click()
    # 调整点击间隔
    sleep(round(uniform(0.4, 0.6), 2))


# 填空题
def fill_textarea(res):
    res.find_element(By.CSS_SELECTOR, '.beginner_problem>textarea').\
        send_keys(chat(get_textarea_question(res)))
    sleep(round(uniform(0.4, 0.6), 2))


# 提交
def submit(driver):
    driver.find_element(By.CSS_SELECTOR, '.submitbtn.mainBgColor').click()
    sleep(5)