def solution(A):
  N = len(A)
  max_left = [0] * N
  max_right = [0] * N
  for i in range(1, N - 1):
    max_left[i] = max(max_left[i - 1] + A[i], 0)
  for i in range(N - 2, 0, -1):
    max_right[i] = max(max_right[i + 1] + A[i], 0)
  max_sum = 0
  for i in range(1, N - 1):
    max_sum = max(max_sum, max_left[i - 1] + max_right[i + 1])
  return max_sum
