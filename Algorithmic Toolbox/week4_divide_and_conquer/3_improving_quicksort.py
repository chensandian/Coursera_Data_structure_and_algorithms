# Uses python3
import sys
import random

def partition3(a, l, r):
    x = a[l]
    small = l
    equal = l
    for i in range(l + 1, r + 1):
        if a[i] < x:
            small += 1
            a[small], a[i] = a[i], a[small]
            equal = max(small, equal)
        if a[i] == x:
            equal += 1
            a[equal], a[i] = a[i], a[equal]
    a[l], a[small] = a[small], a[l]
    return [small, equal]

def partition2(a, l, r):
    x = a[l]
    j = l
    for i in range(l + 1, r + 1):
        if a[i] <= x:
            j += 1
            a[i], a[j] = a[j], a[i]
    a[l], a[j] = a[j], a[l]
    return j


def randomized_quick_sort(a, l, r):
    if l >= r:
        return
    k = random.randint(l, r)
    a[l], a[k] = a[k], a[l]
    #use partition3
    #m = partition2(a, l, r)
    s, e = partition3(a, l, r)
    randomized_quick_sort(a, l, s - 1)
    randomized_quick_sort(a, e + 1, r)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #n, *a = list(map(int, input().split()))
    randomized_quick_sort(a, 0, n - 1)
    for x in a:
        print(x, end=' ')
