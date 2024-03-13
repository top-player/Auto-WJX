# -*- coding: utf-8 -*-
"""
@author: Omen
@time: 2024/3/13 10:09
"""
from openai import OpenAI
import os


def chat(question: str):
    client = OpenAI(api_key=os.getenv("API_KEY"))
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo-0125",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": question + '不少于15字，不超过30字'}
        ],
        max_tokens=200,
        temperature=1.2
    )
    return completion.choices[0].message.content



