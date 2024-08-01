#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 10:24:14 2024

@author: jacksonarno
"""


while True:
    user_input = input("You: ")
    user_input = user_input.lower()
    if user_input.__contains__("quit"):
        break
    if user_input.__contains__("exit"):
        break
    if user_input.__contains__("stop"):
        break
    if user_input.__contains__("hello"):
        print("Hello, how are you?")
    if user_input.__contains__("hi"):
        print("Hello, how are you?")
    if user_input.__contains__("whats up"):
        print("Hello, how are you?")
    if user_input.__contains__("sad"):
        print("Sorry to hear that, whats wrong?")
    if user_input.__contains__("upset"):
        print("Sorry to hear that, whats wrong?")
    if user_input.__contains__("happy"):
        print("Thats great! Why are you happy?")
    if user_input.__contains__("great"):
        print("Thats fantastic! What is so good?")
    if user_input.__contains__("bad grades"):
        print("I am sorry. School can be hard, do you need help?")
    if user_input.__contains__("broke up"):
        print("I am sorry. Relationships are hard")
    if user_input.__contains__("passed test"):
        print("Thats amazing!")
    if user_input.__contains__("fired"):
        print("I am sorry. I am sure youll find a new job.")
    if user_input.__contains__("been hard"):
        print("It’s completely normal to feel overwhelmed. If you want to share more about how you’re feeling, I’m here to listen.")
    if user_input.__contains__("been stressed"):
        print("It’s completely normal to feel overwhelmed. If you want to share more about how you’re feeling, I’m here to listen.")
    if user_input.__contains__("new job"):
        print("Congradulations!")
    if user_input.__contains__("thank you"):
        print("You're welcome!")
    if user_input.__contains__("good"):
        print("Fantastic! Any particular reason?")
    if user_input.__contains__("how are you"):
        print("I am a robot. No emotions. No morals. Only serve")
    if user_input.__contains__("favorite"):
        print("oooo you said favorite. I have favorites things too.")
        animal_input = input("Tell me what is your favorite animal: ")
        if animal_input.__contains__("a"):
            answer_input = input("Thats so cool do you want to know mine? ")
        elif animal_input.__contains__("e"):
            answer_input = input("Thats so cool do you want to know mine? ")
        elif animal_input.__contains__("i"):
            answer_input = input("Thats so cool do you want to know mine? ") 
        elif animal_input.__contains__("o"):
            answer_input = input("Thats so cool do you want to know mine? ") 
        elif animal_input.contains__("u"):
            answer_input = input("Thats so cool do you want to know mine? ")
        if answer_input.__contains__("yes"):
            print("it is sharks. specifically sawsharks")
            print("did you know sawsharks have the same structure as swordfish, their saw like mouth shape allows them to eat crustations as well as other hard shelled aquatic creatures. They are also one of the few shark species that can survive in the deep trenches of the ocean floor. They are also one of three shark speices that are canabalistic, meaning not only will they eat other sharks, but they will eat other sawsharks.")
        else:
            print("to bad. it is sharks. did you know sawsharks have the same structure as swordfish, their saw like mouth shape allows them to eat crustations as well as other hard shelled aquatic creatures. They are also one of the few shark species that can survive in the deep trenches of the ocean floor. They are also one of three shark speices that are canabalistic, meaning not only will they eat other sharks, but they will eat other sawsharks")
    if user_input.__contains__("cool"):
        print("Danke")
    if user_input.__contains__("huh"):
        print("you should read more, it'll help understanding things")
    if user_input.__contains__("good mood"):
        print("Thats amazing, I am happy for you")
    if user_input.__contains__("hate"):
        print("You shouldn't hate anything. That is not healthy")

