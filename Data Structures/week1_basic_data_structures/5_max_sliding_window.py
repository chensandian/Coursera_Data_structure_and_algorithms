# python3
from collections import deque

def max_sliding_window_naive(sequence, m):
    maximums = []
    for i in range(len(sequence) - m + 1):
        maximums.append(max(sequence[i:i + m]))
    return maximums


def max_sliding_window(sequence, m):

    def clean_deque(i):
        if deq and deq[0] == i - m:
            deq.popleft()
        while deq and sequence[i] > sequence[deq[-1]]:
            deq.pop()

    deq = deque()
    max_idx = 0
    for i in range(m):
        clean_deque(i)
        deq.append(i)
        if sequence[i] > sequence[max_idx]:
            max_idx = i
    output = [sequence[max_idx]]

    for i in range(m, n):
        clean_deque(i)
        deq.append(i)
        output.append(sequence[deq[0]])

    return output


if __name__ == '__main__':
    n = int(input())
    input_sequence = [int(i) for i in input().split()]
    assert len(input_sequence) == n
    window_size = int(input())

    #print(*max_sliding_window_naive(input_sequence, window_size))
    print(*max_sliding_window(input_sequence, window_size))

