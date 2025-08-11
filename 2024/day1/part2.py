file = open('input.txt', 'r')

leftNums = []
rightNums = []
score = 0
freqMap = {}

for line in file:
  [left, right] = line.strip().split()
  leftNums.append(int(left))
  rightNums.append(int(right))
  
file.close()

leftNums.sort()
rightNums.sort()

for num in rightNums:
  if num not in freqMap:
    freqMap[num] = 0
  freqMap[num] += 1
  
for num in leftNums:
  if num in freqMap:
    score += freqMap[num] * num
  
print(score)