# Uses python3
import sys

def merge_and_count(a, b):
    c = []
    number_of_inversions = 0
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
            number_of_inversions += len(a) - i
    if i < len(a):
        c += a[i:]
    if j < len(b):
        c += b[j:]
    return c, number_of_inversions

def get_number_of_inversions(a, b, left, right):
    number_of_inversions = 0
    if right - left <= 1:
        return number_of_inversions
    ave = (left + right) // 2
    number_of_inversions += get_number_of_inversions(a, b, left, ave)
    number_of_inversions += get_number_of_inversions(a, b, ave, right)
    a[left:right], count = merge_and_count(a[left:ave], a[ave:right])
    number_of_inversions += count
    return number_of_inversions

if __name__ == '__main__':
    #input = sys.stdin.read()
    #n, *a = list(map(int, input.split()))
    n, *a = list(map(int, input().split()))
    b = n * [0]
    print(get_number_of_inversions(a, b, 0, len(a)))