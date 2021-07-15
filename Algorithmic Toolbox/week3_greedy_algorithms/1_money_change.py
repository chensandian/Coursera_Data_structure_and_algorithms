# Uses python3

def get_change(m):
    min_number = 0
    changes = [10, 5, 1]
    change_index = 0
    while m > 0:
        min_number += m // changes[change_index]
        m = m % changes[change_index]
        change_index += 1
    return min_number

if __name__ == '__main__':
    m = int(input())
    print(get_change(m))
