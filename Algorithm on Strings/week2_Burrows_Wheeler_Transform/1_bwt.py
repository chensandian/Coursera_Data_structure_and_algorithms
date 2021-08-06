# python3
import sys


def BWT(text):
    matrix = []
    double_text = text * 2
    for i in range(len(text)):
        matrix.append(double_text[i:i + len(text)])

    matrix.sort()

    result = ''
    for rotation in matrix:
        result += rotation[-1]

    return result


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    print(BWT(text))
