file = open('input.txt', 'r')

leftNums = []
rightNums = []
diff = 0

for line in file:
  [left, right] = line.strip().split()
  leftNums.append(int(left))
  rightNums.append(int(right))
  
file.close()

leftNums.sort()
rightNums.sort()

for i in range(len(leftNums)):
  diff += abs(leftNums[i] - rightNums[i])
  
print(diff)