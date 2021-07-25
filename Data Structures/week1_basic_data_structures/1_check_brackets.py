# python3

from collections import namedtuple

Bracket = namedtuple("Bracket", ["char", "position"])


def are_matching(left, right):
    return (left + right) in ["()", "[]", "{}"]


def find_mismatch(text):
    opening_brackets_stack = []

    for i, curr in enumerate(text):
        if curr in "([{":
            # Process opening bracket, write your code here
            opening_brackets_stack.append((curr, i))

        if curr in ")]}":
            # Process closing bracket, write your code here
            if not opening_brackets_stack:
                return i + 1
            else:
                prev = opening_brackets_stack.pop()[0]
                result = are_matching(prev, curr)
                if not result:
                    return i + 1

    if not opening_brackets_stack:
        return "Success"
    else:
        return opening_brackets_stack[0][1] + 1



def main():
    text = input()
    mismatch = find_mismatch(text)
    # Printing answer, write your code here
    print(mismatch)

if __name__ == "__main__":
    main()
