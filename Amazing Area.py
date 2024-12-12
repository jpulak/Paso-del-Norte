import math
for i in range(int(input())):
  sas = input().split('-')
  lol= list(map(int,sas))

  side_1 = lol[0]
  side_2 = lol[2]
  angle = lol[1]

  formula = 0.5 * side_1 * side_2 *math.sin(math.radians(angle))

  print("{:.2f}".format(formula))
