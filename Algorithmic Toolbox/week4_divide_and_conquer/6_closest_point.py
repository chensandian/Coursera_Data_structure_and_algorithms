# Uses python3
import sys
import math
import copy


# A class to represent a point in 2D
class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y


# a function to calculate the distance between two points
def distance(p1, p2):
    return math.sqrt((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2)


# a Brute Force method to find the smallest distance when we only have a few points
# P[] of size n
def bruteForce(P, n):
    min_dist = float("inf")
    for i in range(n):
        for j in range(i + 1, n):
            min_dist = min(distance(P[i], P[j]), min_dist)
    return min_dist


# find the closest distance in the strip
# strip is a list containing Points, number of Points is size; each point has |x - midline| <= d
def stripClosest(strip, size, d):
    min_val = d
    for i in range(size):
        j = i + 1
        while j < size and (strip[j].y - strip[i].y) < min_val:
            # the difference in y is already larger than min_val, then the distance will be larger
            min_val = distance(strip[j], strip[i])
            j += 1
    return min_val


# A recursive function used to find the closest distance.
# The list P contains all Points sorted according to Point.x
def closestUntil(p, q, n):
    if n <= 3:
        return bruteForce(p, n)

    # find the middle line
    mid = n // 2
    mid_point = p[mid]

    # keep a copy of left and right parts
    p_left = p[:mid]
    p_right = p[mid:]

    d_left = closestUntil(p_left, q, mid)
    d_right = closestUntil(p_right, q, n - mid)
    d = min(d_left, d_right)

    # stripP = []
    strip_q = []
    # lr = P_left + P_right
    for i in range(n):
        # if abs(lr[i].x - midPoint.x) < d:
        # stripP.append(lr[i])
        if abs(q[i].x - mid_point.x) < d:
            strip_q.append(q[i])

    # stripP.sort(key = lambda point: point.y)
    # min_p = min(d, stripClosest(stripP, len(stripP), d))
    min_q = min(d, stripClosest(strip_q, len(strip_q), d))
    # return min(min_p, min_q)
    return min_q


def minimum_distance(p, n):
    p.sort(key=lambda point: point.x)
    q = copy.deepcopy(p)
    q.sort(key=lambda point: point.y)
    return closestUntil(p, q, n)


if __name__ == '__main__':
    #input = sys.stdin.read()
    input = input()
    data = list(map(int, input.split()))
    n = data[0]
    x = data[1::2]
    y = data[2::2]
    points = []
    for i in range(n):
        points.append(Point(x[i], y[i]))

    print("{0:.5f}".format(minimum_distance(points, n)))
    # print("{0:.9f}".format(bruteForce(points, n)))
