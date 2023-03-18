def solution(A):
  stack = []
  for value in A:
    if not stack:
      stack.append(value)
    elif stack[-1] != value:
      stack.pop()
    else:
      stack.append(value)
  if not stack:
    return -1
  candidate = stack[-1]
  count = 0
  for i, value in enumerate(A):
    if value == candidate:
      count += 1
      if count > len(A) // 2:
        return i
  return -1
