from tree import *
from generation import generate_tree

import os


def preorder(t):
    from functools import reduce
    from operator import add
    return reduce(add, map(preorder, branches(t)), [label(t)])


if __name__ == "__main__":
    os.makedirs('./4/', exist_ok=True)

    for i in range(1, 26):
        with open('./4/{}.in'.format(i), 'w') as fin:
            t = (generate_tree('char', 0))
            fin.write(show_tree(t))
        with open('./4/{}.out'.format(i), 'w') as fout:
            fout.write(str(preorder(t)))

    for i in range(26, 51):
        with open('./4/{}.in'.format(i), 'w') as fin:
            t = (generate_tree('int', 0))
            fin.write(show_tree(t))
        with open('./4/{}.out'.format(i), 'w') as fout:
            fout.write(str(preorder(t)))
