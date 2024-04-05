import re

inputList = []
calTotal = 0
while True:
   line = input()
   if line == "'+":
       break
   else:
       inputList.append(line)

sum = 0
cards = []
for i in inputList:
    myLine = re.split(r'[:|]',i)
    winNums = myLine[1].strip()
    winInts = [int(num) for num in winNums.split()]
    myNums = myLine[2].strip()
    myInts = [int(num) for num in myNums.split()]
    cards.append([winInts, myInts])
for i in cards:
    count = 0
    for j in i[1]:
        if j in i[0]:
            count+=1
    if count > 0:
        sum+= 2 ** (count-1)

print(sum)