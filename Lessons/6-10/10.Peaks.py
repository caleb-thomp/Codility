def solution(A):
  from math import sqrt
  A_len = len(A)
  peaks_until_here = [0] * A_len
  for index in range(1, A_len - 1):
    peaks_until_here[index] = peaks_until_here[index - 1]
    if A[index] > A[index - 1] and A[index] > A[index + 1]:
      peaks_until_here[index] += 1
  if A_len < 3 or peaks_until_here[-2] == 0:
    return 0
  peaks_until_here[-1] = peaks_until_here[-2]
  max_blocks = 0
  for candidate in range(1, int(sqrt(A_len)) + 1, 1):
    if A_len % candidate == 0:
      blocks, block_size = candidate, A_len // candidate
      if peaks_until_here[0] < peaks_until_here[block_size - 1]:
        for each_block in range(block_size, A_len, block_size):
          if peaks_until_here[each_block-1] == \
             peaks_until_here[each_block+block_size-1]:
            break
        else:
          max_blocks = blocks
      if candidate * candidate == A_len:
        continue
      block_size, blocks = candidate, A_len // candidate
      if peaks_until_here[0] < peaks_until_here[block_size - 1]:
        for each_block in range(block_size, A_len, block_size):
          if peaks_until_here[each_block-1] == \
             peaks_until_here[each_block+block_size-1]:
            break
        else:
          return blocks
  return max_blocks
