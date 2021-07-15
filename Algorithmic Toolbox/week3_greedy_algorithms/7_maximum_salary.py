#Uses python3

import sys

class LargerNumKey(str):
    def __lt__(x, y):
        return x+y < y+x

def largest_number(a):
    res = ''.join(sorted(a, key=LargerNumKey, reverse=True))
    return '0' if a[0] == '0' else res

if __name__ == '__main__':
    input = sys.stdin.read()
    data = input.split()
    #data = input().split()
    a = data[1:]
    print(largest_number(a))
