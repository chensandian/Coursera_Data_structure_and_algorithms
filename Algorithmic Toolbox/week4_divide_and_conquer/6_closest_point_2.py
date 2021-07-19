import sys
import math


def distance(point1, point2):
    return math.sqrt((point1[0] - point2[0]) ** 2 + (point1[1] - point2[1]) ** 2)


def brute_force(points, n):
    min_dist = float("inf")
    for i in range(n):
        for j in range(i + 1, n):
            min_dist = min(distance(points[i], points[j]), min_dist)
    return min_dist


def closest_distance_in_strip(points_in_strip, d):
    min_dist = d
    size = len(points_in_strip)
    for i in range(size):
        j = i + 1
        while j < size and (points_in_strip[j][1] - points_in_strip[i][1]) < min_dist:
            min_dist = min(min_dist, distance(points_in_strip[i], points_in_strip[j]))
            j += 1
            if j - i > 7:
                break
    return min_dist


def closest_distance(points_sorted_x, points_sorted_y, n):
    if n < 4:
        return brute_force(points_sorted_x, n)

    mid = n // 2
    points_sorted_x_left = points_sorted_x[:mid]
    points_sorted_x_right = points_sorted_x[mid:]
    points_sorted_y_left = []
    points_sorted_y_right = []
    for point in points_sorted_y:
        if point[0] < points_sorted_x[mid][0]:
            points_sorted_y_left.append(point)
        else:
            points_sorted_y_right.append(point)

    d_left = closest_distance(points_sorted_x_left, points_sorted_y_left, mid)
    d_right = closest_distance(points_sorted_x_right, points_sorted_y_right, n - mid)
    d = min(d_left, d_right)

    points_in_strip = []
    for point in points_sorted_y:
        if point[0] - points_sorted_x[mid][0] < d:
            points_in_strip.append(point)

    return min(d, closest_distance_in_strip(points_in_strip, d))


if __name__ == '__main__':
    data = list(map(int, sys.stdin.read().split()))
    #data = list(map(int, input().split()))
    n = data[0]
    points = [(data[2 * i + 1], data[2 * i + 2]) for i in range(n)]
    points_sorted_x = sorted(points, key=lambda point: point[0])
    points_sorted_y = sorted(points_sorted_x, key=lambda point: point[1])
    print("{0:.9f}".format(closest_distance(points_sorted_x, points_sorted_y, n)))