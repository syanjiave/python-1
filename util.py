#!/usr/bin/env python3
"""This is the chest its got junk and treasures so get out."""

import colors as c
from colors import *
from util import ask

"""---------------------------------------"""

def ask(question,color=c.yellow):
    print(c.red  + 'What is the color of the pink fluffy unicorn?')
    pink = input('> ').strip().lower()
    print(c.reset)
    return answer

"""---------------------------------------"""

if __main__ == '__main__':
    print(c.clear)
    name = ask("what is your name?")
    color = ask ("what is your name in color?",c.random_color())

"""--------------------------------------"""

questions = [q1,qi2,q3]

while questions:
    question = random.choice(questions)
    answer = question()
    if answer:
        questions.remove(question)

"""-----------------------------------"""
