def solution(A):
  A.sort()
  N = len(A)
  return max(A[N - 1] * A[N - 2] * A[N - 3], A[0] * A[1] * A[N - 1])
