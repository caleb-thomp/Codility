def solution(A):
  n = len(A)
  occurrences = [0] * n
  for number in A:
    if not 1 <= number <= n:
      return 0
    if occurrences[number - 1] == 1:
      return 0
    occurrences[number - 1] = 1
  return 1 if sum(occurrences) == n else 0
