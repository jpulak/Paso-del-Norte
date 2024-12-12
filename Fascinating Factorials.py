def unfactorial(n):
    f,i = 1,1
    while f < n:
        i += 1
        f *= i
    return i if f == n else None

for i in range(int(input())):
  print(unfactorial(int(input())))
