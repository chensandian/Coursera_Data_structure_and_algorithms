# Uses python3

def lcm(a, b):
    big, small = max(a, b), min(a, b)
    remainder = 1
    while remainder != 0:
        remainder = big % small
        big = small
        small = remainder
    return int(a * b / big)

if __name__ == '__main__':
    a, b = map(int, input().split())
    print(lcm(a, b))

