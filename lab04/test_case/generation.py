from mobile import *
from tree import *
import numpy as np
import random
import math
import string

MAX_DEPTH = 10
MAX_WEIGHT = 100
MAX_LENGTH = 100
MAX_INT = 100000
BUDGET_FLIP = None
BALANCE_FLIP = None


def generate_random_string(length):
    length = np.random.randint(1, length)
    letters = string.ascii_lowercase
    result_str = ''.join(random.choice(letters) for _ in range(length))
    return result_str

def generate_mobile(element_type: str, depth: int, budget=None, is_balanced=False):
    if element_type == 'planet':
        return planet(budget or np.random.randint(1, MAX_WEIGHT))
    elif element_type == 'arm':
        length, budget = budget or (np.random.randint(1, MAX_LENGTH), None)
        if depth < MAX_DEPTH and np.random.randn() < 0.5 and (not budget or budget > 1):
            return arm(length, generate_mobile('mobile', depth+1, budget, is_balanced))
        else:
            return arm(length, generate_mobile('planet', depth, budget, is_balanced))
    elif element_type == 'mobile':
        if BALANCE_FLIP and np.random.randn() < BALANCE_FLIP:
            is_balanced = not is_balanced
        if not budget and BUDGET_FLIP and np.random.randn() < BUDGET_FLIP:
            budget = np.random.randint(2, MAX_WEIGHT)
        if budget:
            left_weight = np.random.randint(1, budget)
            right_weight = budget - left_weight
            if is_balanced:
                left_length = right_weight // math.gcd(left_weight, right_weight)
                right_length = left_weight // math.gcd(left_weight, right_weight)
            else:
                left_length = np.random.randint(1, MAX_LENGTH)
                right_length = np.random.randint(1, MAX_LENGTH)
            left_budget = (left_length, left_weight)
            right_budget = (right_length, right_weight)
        else:
            left_budget = right_budget = None

        return mobile(generate_mobile('arm', depth, left_budget, is_balanced),
                      generate_mobile('arm', depth, right_budget, is_balanced))


def generate_tree(label_type: str, depth: int):
    if label_type == 'char':
        label = random.choice(string.ascii_lowercase)
    elif label_type == 'int':
        label = np.random.randint(0, MAX_INT)
    else:
        raise NotImplementedError
    if depth < MAX_DEPTH:
        return tree(label, [generate_tree(label_type, depth + 1) for _ in range(np.random.randint(0, 4))])
    else:
        return tree(label)


def generate_list(max_length, max_value):
    length = np.random.randint(0, max_length)
    res = []
    for _ in range(length):
        res.append(np.random.randint(0, max_value))
    return res
