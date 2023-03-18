def solution(S):
  stack = []
  for bracket in S:
    if bracket == '(':
      stack.append(bracket)
    else:
      if not stack:
        return 0
      stack.pop()
  return 1 if not stack else 0
