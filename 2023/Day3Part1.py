import re

inputList = []
calTotal = 0
while True:
   line = input()
   if line == "'+":
       break
   else:
       inputList.append(list(line))

partList = []
numOfCol = len(inputList[0])
numOfRows = len(inputList)
for i in range(len(inputList)):
    started = False
    part = []
    for j in range(len(inputList[i])):
        if inputList[i][j].isdigit() and not started:
            part.append(i)
            part.append(j)
            started = True
            partNum = inputList[i][j]
        elif inputList[i][j].isdigit() and started:
            partNum = partNum + inputList[i][j]
        if not inputList[i][j].isdigit() and started:
            part.append(j-1)
            part.append(int(partNum))
            started = False
            partList.append(part)
            part = []
    if len(part) > 0:
        part.append(j)
        part.append(int(partNum))
        partList.append(part)

def checkIfValid(part):
    rowStart = part[0]-1
    rowEnd = rowStart + 2
    if rowStart < 0: rowStart = 0
    if rowEnd >= numOfRows: rowEnd-=1
    colStart = part[1] - 1
    if colStart < 0: colStart = 0
    colEnd = part[2]+1
    if colEnd >= numOfCol: colEnd-=1
    valid = False
    for i in range(rowStart, rowEnd+1):
        for j in range(colStart, colEnd+1):
            if not inputList[i][j].isdigit() and inputList[i][j] != '.':
                valid = True
    if valid:
        return part[3]
    else:
        return 0
    
sum = 0
for i in partList:
    sum+=checkIfValid(i)

print(sum)