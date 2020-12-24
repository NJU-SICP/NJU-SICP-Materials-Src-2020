from mobile import *
from generation import generate_mobile

import os


def total_weight(m):
    if is_planet(m):
        return size(m)
    else:
        assert is_mobile(m), "must get total weight of a mobile or a planet"
        return total_weight(end(left(m))) + total_weight(end(right(m)))


if __name__ == "__main__":
    os.makedirs('./1/', exist_ok=True)

    for i in range(0, 1):
        with open('./1/{}.in'.format(i), 'w') as fin:
            m = (generate_mobile('planet', 0))
            fin.write(show_mobile(m))
        with open('./1/{}.out'.format(i), 'w') as fout:
            fout.write(str(total_weight(m)))

    for i in range(1, 50):
        with open('./1/{}.in'.format(i), 'w') as fin:
            m = (generate_mobile('mobile', 0))
            fin.write(show_mobile(m))
        with open('./1/{}.out'.format(i), 'w') as fout:
            fout.write(str(total_weight(m)))
