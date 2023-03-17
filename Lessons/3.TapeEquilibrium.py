def solution(A):
  left_sum = A[0]
  right_sum = sum(A[1:])
  min_diff = abs(left_sum - right_sum)

  for i in range(1, len(A) - 1):
    left_sum += A[i]
    right_sum -= A[i]
    diff = abs(left_sum - right_sum)
    if diff < min_diff:
      min_diff = diff
  return min_diff
