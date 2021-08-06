# python3
import sys


def InverseBWT(bwt):
    last_column = [(symbol, index) for index, symbol in enumerate(bwt)]
    first_column = sorted(last_column)
    first_to_last = {first: last for first, last in zip(first_column, last_column)}

    result = ""
    current = first_column[0]
    for i in range(len(bwt)):
        result += current[0]
        current = first_to_last[current]

    return result[::-1]


if __name__ == '__main__':
    bwt = sys.stdin.readline().strip()
    print(InverseBWT(bwt))
