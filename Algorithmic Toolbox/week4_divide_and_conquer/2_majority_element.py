# Uses python3
import sys

def get_majority_element(a, left, right):
    # n==0, so return -1
    if left == right:
        return -1
    # n==1, only 1 number, so a[0] is the majority
    if left + 1 == right:
        return a[left]
    #write your code here (design an O(nlogn) algorithm)
    a.sort()
    while left < right:
        curr = left
        while left + 1 < right and a[left + 1] == a[curr]:
            left += 1
        if (left - curr + 1) > right / 2:
            return 1
        left += 1
    return -1

if __name__ == '__main__':
    input = sys.stdin.read()
    n, *a = list(map(int, input.split()))
    #n, *a = list(map(int, input().split()))
    if get_majority_element(a, 0, n) != -1:
        print(1)
    else:
        print(0)
