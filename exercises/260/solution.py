import math
import numpy as np


def euclidean(a, b):
    m = 0
    for i in range(0, len(a)):
        m = m + (b[i] - a[i]) ** 2
    d = m ** 0.5
    return(d)


def opt_euclidean(a, b):
    m = 0
    for i in range(0, len(a)):
        m = m + math.pow(b[i] - a[i], 2)
    d = math.sqrt(m)
    return(d)


def np_euclidean(a, b):
    m = 0
    for i in range(0, len(a)):
        m = m + np.power(b[i] - a[i], 2)
    d = math.sqrt(m)
    return(d)
