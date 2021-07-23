# Uses python3
import sys


def partition3(nums):
    allsum = sum(nums)
    if allsum % 3 != 0:
        return 0
    nums.sort(reverse=True)
    bucks, subsum = [0] * 3, allsum // 3

    def dfs(index):
        if index == len(nums):
            return len(set(bucks)) == 1
        for i in range(3):
            bucks[i] += nums[index]
            if bucks[i] <= subsum and dfs(index + 1):
                return True
            bucks[i] -= nums[index]
            if bucks[i] == 0:
                break
        return False

    return dfs(0)


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *nums = list(map(int, input.split()))
    if partition3(nums):
        print(1)
    else:
        print(0)

