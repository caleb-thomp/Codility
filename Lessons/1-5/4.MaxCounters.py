def solution(N, A):
  counters = [0] * N
  max_counter = 0
  last_max_counter = 0
  for operation in A:
    if operation <= N:
      counters[operation - 1] = max(counters[operation - 1], last_max_counter)
      counters[operation - 1] += 1
      max_counter = max(max_counter, counters[operation - 1])
    else:
      last_max_counter = max_counter
  for i in range(N):
    counters[i] = max(counters[i], last_max_counter)
  return counters
