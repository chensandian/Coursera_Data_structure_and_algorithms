#Uses python3
import sys

# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.


def build_trie(patterns):
    trie = dict()
    trie[0] = {}
    index = 1

    for pattern in patterns:
        curr = trie[0]
        for letter in pattern:
            if letter in curr:
                curr = trie[curr[letter]]   # move to the dict of next node
            else:
                curr[letter] = index    # add to current node
                trie[index] = {}
                curr = trie[index]
                index += 1

    return trie


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
