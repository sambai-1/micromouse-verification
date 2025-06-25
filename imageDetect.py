import numpy as np


def findDifference(side, difference):
    half = side // 2
    square = [[1] * side for _ in range(side)]
    square = np.array(square)
    h, w = difference.shape

    prevBest = -1
    bestCenter = (0, 0)

    for y in range(half, h - half, 5):  # step = 5
        for x in range(half, w - half, 5):
            area = difference[y - half : y + half, x - half : x + half]
            if area.shape != square.shape:
                print("wrong")
                continue

            curr = np.sum(area * square)
            if curr > prevBest:
                prevBest = curr
                bestCenter = (x, y)
    return bestCenter