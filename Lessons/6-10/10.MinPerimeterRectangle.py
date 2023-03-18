def solution(N):
   min_perimeter = float('inf')
   for i in range(1, int(N**0.5) + 1):
       if N % i == 0:
           perimeter = 2 * (i + N//i)
           min_perimeter = min(min_perimeter, perimeter)
   return min_perimeter
