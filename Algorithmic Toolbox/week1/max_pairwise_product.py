# python3


def max_pairwise_product(numbers):
    n = len(numbers)
    large1 = 0
    large2 = 0
    for num in numbers:
        if num > large1:
            large2 = large1
            large1 = num
        elif num > large2:
            large2 = num
    return large1 * large2


if __name__ == '__main__':
    input_n = int(input())
    input_numbers = [int(x) for x in input().split()]
    print(max_pairwise_product(input_numbers))
