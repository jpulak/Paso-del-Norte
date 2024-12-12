n= int(input())
heh=[]
for i in range(n):
  lower = 0
  upper= int(input())
  for num in range(lower, upper + 1):
   # all prime numbers are greater than 1
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           heh.append(num)
  print(sum(heh))
  heh=[]
    
