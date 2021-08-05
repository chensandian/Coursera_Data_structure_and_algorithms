# python3
import sys


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


def prefix_trie_matching(text, trie):
	index = 0
	symbol = text[index]
	curr = trie[0]

	while True:
		if not curr:
			return True
		elif symbol in curr:
			curr = trie[curr[symbol]]
			index += 1
			if index < len(text):
				symbol = text[index]
			else:
				symbol = "$"
		else:
			return False


def solve(text, n, patterns):
	result = []
	trie = build_trie(patterns)

	for start_index in range(len(text)):
		if prefix_trie_matching(text[start_index:], trie):
			result.append(start_index)
	return result


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
	patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)
sys.stdout.write(' '.join(map(str, ans)) + '\n')