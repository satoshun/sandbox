import math
import random


def kmeans(vector, K):
    data = []
    # initialize
    for v in vector:
        data += [v, random.randint(0, K-1)]

    # calculate center of gravity
    centers = []
    for k in range(K):
        vv = []
        for v in data:
            if v[0] == k:
                vv.append(v)
        vv

    return data


def center(points):
    pass


def _distance(v1, v2):
    '''Euclidean metric'''
    distance = 0.0
    for p1, p2 in zip(v1, v2):
        distance += (p1 - p2) ** 2
    return math.sqrt(distance)


if __name__ == '__main__':
    data = [
        [1, 0, 1, 0],
        [1, 1, 1, 0],
        [0, 0, 0, 0],
        [1, 0, 0, 0],
        [1, 0, 0, 1],
        [1, 0, 1, 1],
    ]

    kmeans(data, 2)
