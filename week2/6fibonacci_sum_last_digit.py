# Uses python3

def fibonacci_sum(n):
    if n <= 1:
        return n

    previous = 0
    current = 1
    sums = [0, 1]

    for _ in range(60):
        previous, current = current, previous + current
        sums.append((sums[-1] + current) % 10)

    return sums[n % 60] if n > 60 else sums[n]

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum(n))
