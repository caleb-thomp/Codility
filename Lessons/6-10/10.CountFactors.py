def solution(N):
  num_factors = 0
  for i in range(1, int(N**0.5) + 1):
    if N % i == 0:
      num_factors += 2
  if int(N**0.5)**2 == N:
    num_factors -= 1
  return num_factors
