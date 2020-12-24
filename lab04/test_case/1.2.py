from mobile import *
from generation import generate_mobile

import os
import numpy as np


def balanced(m):
    def torque(arm):
        return total_weight(end(arm)) * length(arm)

    if is_planet(m):
        return True
    return balanced(end(left(m))) and balanced(end(right(m))) and \
        torque(left(m)) == torque(right(m))


if __name__ == "__main__":
    os.makedirs('./2/', exist_ok=True)


    for i in range(1, 6):
        with open('./2/{}.in'.format(i), 'w') as fin:
            m = (generate_mobile('planet', 0))
            fin.write(show_mobile(m))
        with open('./2/{}.out'.format(i), 'w') as fout:
            fout.write(str(balanced(m)))

    for i in range(6, 31):
        with open('./2/{}.in'.format(i), 'w') as fin:
            budget = np.random.randint(20000)
            m = (generate_mobile('mobile', 0, budget, True))
            fin.write(show_mobile(m))
        with open('./2/{}.out'.format(i), 'w') as fout:
            fout.write(str(balanced(m)))

    for i in range(31, 36):
        with open('./2/{}.in'.format(i), 'w') as fin:
            budget = np.random.randint(20000)
            m = (generate_mobile('mobile', 0, budget))
            fin.write(show_mobile(m))
        with open('./2/{}.out'.format(i), 'w') as fout:
            fout.write(str(balanced(m)))

    for i in range(36, 51):
        with open('./2/{}.in'.format(i), 'w') as fin:
            m = (generate_mobile('mobile', 0))
            fin.write(show_mobile(m))
        with open('./2/{}.out'.format(i), 'w') as fout:
            fout.write(str(balanced(m)))
