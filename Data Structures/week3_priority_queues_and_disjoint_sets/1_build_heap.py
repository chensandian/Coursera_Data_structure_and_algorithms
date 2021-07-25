# python3
# use a min heap

def parent(i):
    return (i - 1) // 2


def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


def sift_up(i):
    while i > 0 and nums[parent(i)] > nums[i]:
        nums[parent(i)], nums[i] = nums[i], nums[parent(i)]
        i = parent(i)


def sift_down(i):
    min_index = i
    size = len(nums)
    while i < size:
        left = left_child(i)
        if left < size and nums[left] < nums[min_index]:
            min_index = left
        right = right_child(i)
        if right < size and nums[right] < nums[min_index]:
            min_index = right
        if i != min_index:
            nums[i], nums[min_index] = nums[min_index], nums[i]
            swaps.append((i, min_index))
            i = min_index
        else:
            break


def build_heap(nums):
    size = len(nums)
    start = (size - 2) // 2
    for index in range(start, -1, -1):
        sift_down(index)


def build_heap_naive(data):
    """Build a heap from ``data`` inplace.

    Returns a sequence of swaps performed by the algorithm.
    """
    # The following naive implementation just sorts the given sequence
    # using selection sort algorithm and saves the resulting sequence
    # of swaps. This turns the given array into a heap, but in the worst
    # case gives a quadratic number of swaps.
    #
    # replace by a more efficient implementation
    swaps = []
    for i in range(len(data)):
        for j in range(i + 1, len(data)):
            if data[i] > data[j]:
                swaps.append((i, j))
                data[i], data[j] = data[j], data[i]
    return swaps


if __name__ == "__main__":
    n = int(input())
    nums = list(map(int, input().split()))
    assert len(nums) == n

    swaps = []
    build_heap(nums)

    print(len(swaps))
    for i, j in swaps:
        print(i, j)
