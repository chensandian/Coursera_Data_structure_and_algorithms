# python3
import sys


def sort_characters(string):
    order = [-1 for _ in range(len(string))]
    count = [0 for _ in range(5)]  # contain $ A T C G only
    for i in range(len(string)):
        count[symbols[string[i]]] += 1
    for j in range(1, 5):
        count[j] = count[j] + count[j - 1]
    for i in range(len(string) - 1, -1, -1):
        c = symbols[string[i]]
        count[c] -= 1
        order[count[c]] = i
    return order


def compute_character_classes(string, order):
    classes = [0 for _ in range(len(string))]
    for i in range(1, len(string)):
        if string[order[i]] != string[order[i - 1]]:
            classes[order[i]] = classes[order[i - 1]] + 1
        else:
            classes[order[i]] = classes[order[i - 1]]
    return classes


def sort_doubled(string, current_length, order, classes):
    count = [0 for _ in range(len(string))]
    new_order = [-1 for _ in range(len(string))]
    for i in range(len(string)):
        count[classes[i]] = count[classes[i]] + 1
    for j in range(1, len(string)):
        count[j] = count[j] + count[j - 1]
    for i in range(len(string) - 1, -1, -1):
        start = (order[i] - current_length + len(string)) % len(string)
        cl = classes[start]
        count[cl] = count[cl] - 1
        new_order[count[cl]] = start
    return new_order


def update_classes(new_order, classes, current_length):
    n = len(new_order)
    new_classes = [0] * n
    for i in range(1, n):
        curr = new_order[i]
        prev = new_order[i - 1]
        mid = curr + current_length
        mid_prev = (prev + current_length) % n
        if classes[curr] != classes[prev] or classes[mid] != classes[mid_prev]:
            new_classes[curr] = new_classes[prev] + 1
        else:
            new_classes[curr] = new_classes[prev]
    return new_classes


def build_suffix_array(text):
    """
    Build suffix array of the string text and
    return a list result of the same length as the text
    such that the value result[i] is the index (0-based)
    in text where the i-th lexicographically smallest
    suffix of text starts.
    """
    result = []
    order = sort_characters(text)
    classes = compute_character_classes(text, order)
    current_length = 1
    while current_length < len(text):
        order = sort_doubled(text, current_length, order, classes)
        classes = update_classes(order, classes, current_length)
        current_length = current_length * 2
    return order


if __name__ == '__main__':
    text = sys.stdin.readline().strip()
    symbols = {"$": 0, "A": 1, "T": 4, "C": 2, "G": 3}
    print(" ".join(map(str, build_suffix_array(text))))
