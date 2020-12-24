from mobile import *
from tree import *
from generation import generate_mobile

import os


def totals_tree(m):
    if is_planet(m):
        return tree(size(m))
    subtrees = [totals_tree(end(left(m))), totals_tree(end(right(m)))]
    return tree(label(subtrees[0]) + label(subtrees[1]), subtrees)


if __name__ == "__main__":
    os.makedirs('./3/', exist_ok=True)

    for i in range(1, 3):
        with open('./3/{}.in'.format(i), 'w') as fin:
            m = (generate_mobile('planet', 0))
            fin.write(show_mobile(m))
        with open('./3/{}.out'.format(i), 'w') as fout:
            fout.write(str(totals_tree(m)))

    for i in range(3, 51):
        with open('./3/{}.in'.format(i), 'w') as fin:
            m = (generate_mobile('mobile', 0))
            fin.write(show_mobile(m))
        with open('./3/{}.out'.format(i), 'w') as fout:
            fout.write(str(totals_tree(m)))
