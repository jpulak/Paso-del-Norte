oh = int(input())
nums = []
for i in range(oh):
  nums.append(input().split())

well = []
for i in range(oh):
  ah = []
  for n in range(4): 
    if n == 0:
      ah.append(int(nums[i][0]) + int(nums[i][1]))
    if n == 1:
      ah.append(int(nums[i][0]) * int(nums[i][1]))
    if n == 2:
      ah.append(int(nums[i][0]) - int(nums[i][1]))
    if n == 3:
      ah.append(int(nums[i][0]) / int(nums[i][1]))
  for m in range(4):
    b = "{:.2f}".format(ah[m])
    if b[-1]=="0" and b[-2] == "0":
      if b[0]=="0":
        print((str(ah[m][1::])), end=" ")
      else:
        print((str(ah[m])), end=" ")
    else:
      if b[0]=="0":
        print(str(b)[1::], end=" ")
      else:
        print(str(b), end=" ")
    
  print(" ")


