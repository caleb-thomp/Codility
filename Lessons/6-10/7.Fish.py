def solution(A, B):
  stack = []
  count = 0
  for i in range(len(A)):
    if B[i] == 1:
      stack.append(A[i])
    else:
      while stack and stack[-1] < A[i]:
        stack.pop()
      if not stack:
        count += 1
  return count + len(stack)
