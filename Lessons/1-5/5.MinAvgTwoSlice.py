def solution(A):
  N = len(A)
  min_avg = (A[0] + A[1]) / 2
  min_index = 0
  for i in range(2, N):
    avg2 = (A[i - 1] + A[i]) / 2
    avg3 = (A[i - 2] + A[i - 1] + A[i]) / 3
    if avg2 < min_avg:
      min_avg = avg2
      min_index = i - 1
    if avg3 < min_avg:
      min_avg = avg3
      min_index = i - 2
  return min_index
