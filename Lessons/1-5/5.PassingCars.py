def count_passing_cars(A):
  N = len(A)
  prefix_sum = [0] * (N + 1)
  for i in range(1, N + 1):
    prefix_sum[i] = prefix_sum[i - 1] + A[i - 1]
  count = 0
  for i in range(N):
    if A[i] == 0:
      count += prefix_sum[N] - prefix_sum[i + 1]
    if count > 1000000000:
      return -1
  return count
