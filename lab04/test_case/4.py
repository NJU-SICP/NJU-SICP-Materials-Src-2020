from tree import *
from generation import generate_list

import os
import numpy as np
import random

def insert_items(lst, entry, elem):
    index = 0
    while index < len(lst):
        if lst[index] == entry:
            lst.insert(index + 1, elem)
            if entry == elem:
                index += 1
        index += 1
    return lst


if __name__ == "__main__":
    os.makedirs('./6/', exist_ok=True)

    for i in range(1, 26):
        with open('./6/{}.in'.format(i), 'w') as fin:
            ls = generate_list(100, 100)
            elem = np.random.randint(0, 100)
            target_elem = np.random.randint(0, 200)
            fin.write(str(ls) + '\n')
            fin.write(str(elem) + '\n')
            fin.write(str(target_elem))
        with open('./6/{}.out'.format(i), 'w') as fout:
            fout.write(str(insert_items(ls, elem, target_elem)))

    for i in range(26, 46):
        with open('./6/{}.in'.format(i), 'w') as fin:
            ls = generate_list(10000, 10000)
            elem = np.random.randint(0, 20000)
            target_elem = np.random.randint(0, 50000)
            fin.write(str(ls) + '\n')
            fin.write(str(elem) + '\n')
            fin.write(str(target_elem))
        with open('./6/{}.out'.format(i), 'w') as fout:
            fout.write(str(insert_items(ls, elem, target_elem)))

    for i in range(46, 51):
        with open('./6/{}.in'.format(i), 'w') as fin:
            ls = generate_list(10000, 10000)
            elem = random.choices(ls)[0]
            target_elem = np.random.randint(0, 50000)
            fin.write(str(ls) + '\n')
            fin.write(str(elem) + '\n')
            fin.write(str(target_elem))
        with open('./6/{}.out'.format(i), 'w') as fout:
            fout.write(str(insert_items(ls, elem, target_elem)))