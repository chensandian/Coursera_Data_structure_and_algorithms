# Uses python3
def calc_fib(n):
    if (n <= 1):
        return n
    prev2 = 0
    prev1 = 1
    i = 1
    while i < n:
        curr = prev2 + prev1
        i += 1
        if i == n:
            return curr
        else:
            prev2 = prev1
            prev1 = curr

n = int(input())
print(calc_fib(n))
