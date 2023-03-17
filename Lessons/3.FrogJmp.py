import math


def solution(X, Y, D):
  distance = Y - X
  jumps = math.ceil(distance / D)
  return jumps
