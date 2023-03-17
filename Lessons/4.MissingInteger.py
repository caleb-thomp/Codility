def solution(A):
  A = [num for num in A if num > 0]
  if not A:
    return 1
  A.sort()
  if A[0] > 1:
    return 1
  for i in range(len(A) - 1):
    if A[i + 1] - A[i] > 1:
      return A[i] + 1
  return A[-1] + 1
