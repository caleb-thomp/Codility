def solution(numbers):
  """Solution method implementation."""
  # initialize start and end lists
  disc_start = []
  disc_end = []
  # build the start and end lists
  for i, item in enumerate(numbers):
    disc_start.append(i - item)
    disc_end.append(i + item)
  # sort the two lists in ascending order
  disc_start.sort()
  disc_end.sort()
  # initialize other variables
  open_discs = 0
  intersections = 0
  k = 0
  list_len = len(numbers)
  # iterate through the start list
  for i in range(list_len):
    # iterate through the end list
    for j in range(k, list_len):
      # we open a disc
      if disc_start[i] <= disc_end[j]:
        intersections += open_discs
        # too many intersections
        if intersections > 10000000:
          return -1
        open_discs += 1
        break
      # close a disc
      open_discs -= min(1, open_discs)
      k += 1
  # return the result
  return intersections
