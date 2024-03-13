# -*- coding: utf-8 -*-
"""
@author: Omen
@time: 2024/3/12 13:02
"""
from func.funcs import *


def main():
    # 问卷地址
    url = '**************'
    driver = load_driver(url)
    res = get_all_questions(driver)
    # 题目计数
    num_questions = len(res)
    num_question = 0
    for i in res:
        if is_radio(i) == 'radio':
            click_radio(i)
            num_question += 1
        elif is_radio(i) == 'checkbox':
            click_checkbox(i)
            num_question += 1
        elif is_radio(i) == 'textarea':
            fill_textarea(i)
            num_question += 1
        else:
            continue
    if num_question == num_questions:
        submit(driver)
        print('提交成功')
    else:
        print('还有题目没做完，提交失败')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
