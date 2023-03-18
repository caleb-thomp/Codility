def solution(A):
  expected_sum = (len(A) + 1) * (len(A) + 2) // 2
  actual_sum = sum(A)
  return expected_sum - actual_sum
