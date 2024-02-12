def fibonacci(num):
  # Edge cases
  if num == 0:
    return 0
  elif num == 1:
    return 1

  # Set first terms
  twoBack = 0
  oneBack = 1
  current = 0

  # Iterate over n sequences past 2nd term
  for x in range(num, 1, -1):
    current = oneBack + twoBack
    twoBack = oneBack
    oneBack = current

  return current
