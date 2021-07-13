# Uses python3

def get_fibonacci_huge(n, m):
    nums = [0, 1]
    if n <= 1:
        return nums[n]

    index = 2
    while index <= n:
        nums.append((nums[index-1] + nums[index-2]) % m)
        index += 1
        if nums[-2] == 0 and nums[-1] == 1:
            return nums[n % (index-2)]
    return nums[n]



if __name__ == '__main__':
    n, m = map(int, input().split())
    print(get_fibonacci_huge(n, m))
