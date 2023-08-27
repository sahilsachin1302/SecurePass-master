from collections import Counter
from math import log


def shannon(str):
    counts = Counter(str)
    frequencies = ((i / len(str)) for i in counts.values())
    return - sum(f * log(f, 2) for f in frequencies)


def chronic_theta(num):
    if num > 1:
        return 1
    else:
        return num


def encode(str):
    encode = shannon(str)/4
    return chronic_theta(encode)


if __name__ == '__main__':
    encode(str)
