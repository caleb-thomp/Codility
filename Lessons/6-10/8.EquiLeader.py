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
    return 0
  candidate = stack[-1]
  count = A.count(candidate)
  if count <= len(A) // 2:
    return 0
  leader_count = 0
  equi_leader_count = 0
  for i, value in enumerate(A):
    if value == candidate:
      leader_count += 1
    if leader_count > (i + 1) // 2 and count - leader_count > (len(A) - i -
                                                               1) // 2:
      equi_leader_count += 1
  return equi_leader_count
