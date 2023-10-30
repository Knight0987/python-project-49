from math import gcd
import random


GAME_TASK = 'Find the greatest common divisor of given numbers.'


def game_task():
    first_value = random.randint(1, 100)
    second_value = random.randint(1, 100)
    question = f"{first_value} {second_value}"
    correct_answer = str(gcd(first_value, second_value))
    return question, correct_answer
