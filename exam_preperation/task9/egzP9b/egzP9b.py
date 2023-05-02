from egzP9btesty import runtests
from collections import deque


def dyrektor(G, R):

	n = len(G)
	x = [[0 for _ in range(n)] for _ in range(n)]
	idx = [0 for _ in range(n)]
	for i in range(n):
		for j in G[i]:
			x[i][j] += 1
		for j in R[i]:
			x[i][j] -= 1

	result = deque()
	u = 0
	v = [0]
	flag = True

	while flag:
		while idx[u] < n and x[u][idx[u]] == 0:
			idx[u] += 1
		if idx[u] >= n:
			result.appendleft(u)
			v.pop()
			if len(v) == 0:
				flag = False
			else:
				u = v[-1]
			continue
		x[u][idx[u]] -= 1
		v.append(idx[u])
		u = idx[u]

	return result


runtests(dyrektor, all_tests=True)
