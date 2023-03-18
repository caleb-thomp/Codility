def solution(A, K):
  N = len(A)
  if N == 0:
    return A
  K = K % N
  if K == 0:
    return A
  else:
    return A[N - K:] + A[:N - K]
