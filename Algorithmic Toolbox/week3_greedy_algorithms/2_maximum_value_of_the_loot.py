# Uses python3
import sys
def get_optimal_value(capacity, weights, values):
    max_value = 0
    unit_values = [(values[index] / weights[index], index) for index in range(len(weights))]
    unit_values.sort(reverse = True)
    item_number = 0
    while capacity > 0 and item_number < len(weights):
        # find weight we can get from the item
        weight = min(capacity, weights[unit_values[item_number][1]])
        capacity -= weight
        max_value += weight * unit_values[item_number][0]
        item_number += 1

    return max_value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    #data = list(map(int, input().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    # output answer with at least four digits after the decimal point
    print("{:.10f}".format(opt_value))
