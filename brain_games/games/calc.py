import random
import operator


GAME_TASK = 'What is the result of the expression?'


def game_task():
    first_value = random.randint(1, 100)
    second_value = random.randint(1, 100)
    operators = {
        '+': operator.add,
        '-': operator.sub,
        '*': operator.mul
    }
    operator_symb = random.choice(list(operators))
    question = f"{first_value} {operator_symb} {second_value}"
    correct_answer = str(operators.get(operator_symb)(first_value, second_value))
    return question, correct_answer
