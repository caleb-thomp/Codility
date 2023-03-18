def solution(A):
  occurrences = {}
  for element in A:
    if element in occurrences:
      occurrences[element] += 1
    else:
      occurrences[element] = 1
  for element, count in occurrences.items():
    if count % 2 == 1:
      return element
