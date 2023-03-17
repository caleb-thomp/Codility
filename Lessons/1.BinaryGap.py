def solution(N):
  binary = bin(N)[2:]  # convert N to binary and remove '0b' prefix
  max_gap = 0
  current_gap = 0
  for digit in binary:
    if digit == '0':
      current_gap += 1
    elif digit == '1':
      if current_gap > max_gap:
        max_gap = current_gap
      current_gap = 0
  return max_gap
