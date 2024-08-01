#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 09:02:53 2024

@author: jacksonarno
"""

import openai

openai.api_key = "sk-proj-as1hWQeuR83B14fpx9LBT3BlbkFJK9ad2a252rmI62dxIaHz"

def chat_with_gpt(prompt):
     response = openai.ChatCompletion.create(
         model = "gpt-3",
         messages = [{"role": "user", "content": prompt}]
         )
     return response.choices[0].message.content.strip()
 
if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "exit", "bye", "stop", "end"]:
            break
        
        response = chat_with_gpt(user_input)
        print("BabyChatBot: ", response)