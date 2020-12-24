from tree import *
from generation import *

import os


def sample_tree(t):
    if not is_leaf(t) and np.random.randn() < 0.8:
        branch = random.choice(branches(t))
        return label(t) + sample_tree(branch)
    else:
        return label(t)


def sample_tree_with_skip(t):
    if not is_leaf(t) and np.random.randn() < 0.8:
        branch = random.choice(branches(t))
        if np.random.randn() < 0.5:
            return label(t) + sample_tree(branch)
        else:
            return sample_tree(branch)
    else:
        return label(t)


def has_path(t, word):
    assert len(word) > 0, 'no path for empty word.'
    if label(t) != word[0]:
        return False
    if len(word) == 1:
        return True
    for subtree in branches(t):
        if has_path(subtree, word[1:]):
            return True
    return False


if __name__ == "__main__":
    os.makedirs('./5/', exist_ok=True)

    for i in range(1, 26):
        with open('./5/{}.in'.format(i), 'w') as fin:
            t = (generate_tree('char', 0))
            target_str = generate_random_string(MAX_DEPTH)
            fin.write(show_tree(t) + '\n')
            fin.write(target_str)
        with open('./5/{}.out'.format(i), 'w') as fout:
            fout.write(str(has_path(t, target_str)))

    for i in range(26, 36):
        with open('./5/{}.in'.format(i), 'w') as fin:
            t = (generate_tree('char', 0))
            target_str = sample_tree(t)
            fin.write(show_tree(t) + '\n')
            fin.write(target_str)
        with open('./5/{}.out'.format(i), 'w') as fout:
            fout.write(str(has_path(t, target_str)))

    for i in range(36, 51):
        with open('./5/{}.in'.format(i), 'w') as fin:
            t = (generate_tree('char', 0))
            target_str = sample_tree_with_skip(t)
            fin.write(show_tree(t) + '\n')
            fin.write(target_str)
        with open('./5/{}.out'.format(i), 'w') as fout:
            fout.write(str(has_path(t, target_str)))

