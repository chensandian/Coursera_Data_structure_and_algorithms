# Uses python3
import sys


def optimal_sequence(n):
    if len(min_sequence_list[n]) > 1:
        return min_sequence_list[n][0]

    min_num_3 = min_num_2 = min_num_1 = n
    if n % 3 == 0:
        min_num_3 = optimal_sequence(n // 3) + 1
    if n % 2 == 0:
        min_num_2 = optimal_sequence(n // 2) + 1
    if n > 1:
        min_num_1 = optimal_sequence(n - 1) + 1

    min_num = min(min_num_1, min_num_2, min_num_3)
    if min_num_1 == min_num:
        min_sequence_list[n] = [min_num] + min_sequence_list[n - 1][1:] + [n]
    elif min_num_2 == min_num:
        min_sequence_list[n] = [min_num] + min_sequence_list[n // 2][1:] + [n]
    elif min_num_3 == min_num:
        min_sequence_list[n] = [min_num] + min_sequence_list[n // 3][1:] + [n]
    return min_num


input = sys.stdin.read()
num = int(input)
min_sequence_list = [[0] for i in range(num + 1)]
min_sequence_list[1] = [0, 1]
for i in range(1,num + 1):
    optimal_sequence(i)
print(min_sequence_list[num][0])
for num in min_sequence_list[num][1:]:
    print(num, end=' ')

