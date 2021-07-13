# Uses python3
# F0^2 + F1^2 + ... + Fn^2 = F(n) * F(n+1)
# last digit of the sum = last digit of F(n) * last digit of F(n+1) % 10

def get_fibonacci_last_digit(n):
    if n <= 1:
        return n

    previous = 0
    current = 1

    for _ in range(n - 1):
        previous, current = current, (previous + current) % 10

    return current

def fibonacci_sum_squares(n):
    return (get_fibonacci_last_digit(n % 60) * get_fibonacci_last_digit((n + 1) % 60)) % 10

if __name__ == '__main__':
    n = int(input())
    print(fibonacci_sum_squares(n))
