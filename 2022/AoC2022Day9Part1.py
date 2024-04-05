import math
inputList = []
while True:
   line = input()
   if line == "'++'":
       break
   else:
       inputList.append(line)

hPos = [0,0]
tPos = [0,0]
posList = []

def fixDiag(hPos,xPosDif,yPosDif):
    if xPosDif > 1:  
        return [hPos[0]-1,hPos[1]]
    elif xPosDif < -1:  
        return [hPos[0]+1,hPos[1]]
    elif yPosDif > 1:  
        return [hPos[0],hPos[1]-1]
    elif yPosDif < -1:  
        return [hPos[0],hPos[1]+1]

def checkRelation(hPos,tPos):
    xPosDif = hPos[0]-tPos[0]
    yPosDif = hPos[1]-tPos[1]
    if abs(xPosDif) > 1 and abs(yPosDif) == 1 or abs(yPosDif) > 1 and abs(xPosDif) == 1:
        tPos = fixDiag(hPos,xPosDif,yPosDif)
    elif xPosDif > 1:
        tPos = [hPos[0]-1,hPos[1]]
    elif xPosDif < -1:
        tPos = [hPos[0]+1,hPos[1]]
    elif yPosDif > 1:
        tPos = [hPos[0],hPos[1]-1]
    elif yPosDif < -1:
        tPos = [hPos[0],hPos[1]+1]
    return tPos

for i in inputList:
    lineList = i.split(' ')
    for j in range(int(lineList[1])):
        if lineList[0] == 'L':
            hPos[0] = hPos[0] - 1
        elif lineList[0] == 'R':
            hPos[0] = hPos[0] + 1
        elif lineList[0] == 'U':
            hPos[1] = hPos[1] + 1
        elif lineList[0] == 'D':
            hPos[1] = hPos[1] - 1
        tPos = checkRelation(hPos,tPos)
        if tPos not in posList:
            posList.append(tPos)
            
print(len(posList))