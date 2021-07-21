# Uses python3
import sys

def get_change(m):
    if min_num_list[m] != 0:
        return min_num_list[m]

    min_num = m
    for coin in coins:
        if m >= coin:
            min_num = min(min_num, get_change(m - coin) + 1)
    min_num_list[m] = min_num
    return min_num

if __name__ == '__main__':
    m = int(sys.stdin.read())
    #m = int(input())
    coins = [1, 3, 4]
    min_num_list = [0] * (m + 1)
    print(get_change(m))
