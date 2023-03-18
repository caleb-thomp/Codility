def solution(brackets):
  stack = []
  for bracket in brackets:
    if bracket in ['(', '{', '[']:
      stack.append(bracket)
    else:
      if not stack:
        return 0
      top_bracket = stack.pop()
      if (top_bracket == '(' and bracket != ')') or \
         (top_bracket == '{' and bracket != '}') or \
         (top_bracket == '[' and bracket != ']'):
        return 0
  return 1 if not stack else 0
