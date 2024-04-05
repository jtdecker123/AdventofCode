import math
inputList = []
while True:
   line = input()
   if line == "'++'":
       break
   else:
       inputList.append(line)

hPos = [0,0]
pos1 = [0,0]
pos2 = [0,0]
pos3 = [0,0]
pos4 = [0,0]
pos5 = [0,0]
pos6 = [0,0]
pos7 = [0,0]
pos8 = [0,0]
pos9 = [0,0]
posList = []

def fixDiag(hPos,tPos,xPosDif,yPosDif):
    if xPosDif > 1:
        if yPosDif > 1:
            return [tPos[0]+1,tPos[1]+1]
        elif yPosDif < -1:
            return [tPos[0]+1,tPos[1]-1]
        return [hPos[0]-1,hPos[1]]
    elif xPosDif < -1:  
        if yPosDif > 1:
            return [tPos[0]-1,tPos[1]+1]
        elif yPosDif < -1:
            return [tPos[0]-1,tPos[1]-1]
        return [hPos[0]+1,hPos[1]]
    elif yPosDif > 1:  
        if xPosDif > 1:
            return [tPos[0]+1,tPos[1]+1]
        elif xPosDif < -1:
            return [tPos[0]-1,tPos[1]+1]
        return [hPos[0],hPos[1]-1]
    elif yPosDif < -1:
        if xPosDif > 1:
            return [tPos[0]+1,tPos[1]-1]
        elif xPosDif < -1:
            return [tPos[0]-1,tPos[1]-1]  
        return [hPos[0],hPos[1]+1]

def checkRelation(hPos,tPos):
    xPosDif = hPos[0]-tPos[0]
    yPosDif = hPos[1]-tPos[1]
    if abs(xPosDif) > 1 and abs(yPosDif) >= 1 or abs(yPosDif) > 1 and abs(xPosDif) >= 1:
        tPos = fixDiag(hPos,tPos,xPosDif,yPosDif)
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
        pos1 = checkRelation(hPos,pos1)
        pos2 = checkRelation(pos1,pos2)
        pos3 = checkRelation(pos2,pos3)
        pos4 = checkRelation(pos3,pos4)
        pos5 = checkRelation(pos4,pos5)
        pos6 = checkRelation(pos5,pos6)
        pos7 = checkRelation(pos6,pos7)
        pos8 = checkRelation(pos7,pos8)
        pos9 = checkRelation(pos8,pos9)
        if pos9 not in posList:
            posList.append(pos9)
            
print(len(posList))