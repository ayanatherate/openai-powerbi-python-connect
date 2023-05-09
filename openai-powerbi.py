# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import openai

openai.api_key = "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"
model_engine = "text-davinci-002"

prompt = 'Write a DAX query for capitalizing Strings'

response = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,n=1,stop=None,temperature=0.7
)

answer = response.choices[0].text.strip()
print("Answer:", answer)