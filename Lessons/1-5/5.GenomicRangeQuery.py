def solution(S, P, Q):
  N = len(S)
  M = len(P)
  impact_factor = {'A': 1, 'C': 2, 'G': 3, 'T': 4}
  prefix_sum = [[0] * 4 for _ in range(N + 1)]
  for i in range(1, N + 1):
    nucleotide = S[i - 1]
    impact = impact_factor[nucleotide]
    prefix_sum[i][impact - 1] = prefix_sum[i - 1][impact - 1] + 1
    for j in range(4):
      if j != impact - 1:
        prefix_sum[i][j] = prefix_sum[i - 1][j]
  result = []
  for i in range(M):
    start, end = P[i], Q[i] + 1
    for j in range(4):
      if prefix_sum[end][j] - prefix_sum[start][j] > 0:
        result.append(j + 1)
        break
  return result
