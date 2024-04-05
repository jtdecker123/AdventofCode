inputList = []
fullLine = ''
while True:
    line = input()
    if line == "'+":
       inputList.append(fullLine)
       break
    if line == '':
        inputList.append(fullLine)
        fullLine = ''
    else: 
        fullLine = fullLine + ' ' + line
        fullLine = fullLine.lstrip()
    
seedList = []
seedSplit = inputList[0].split(':')[1]
seedSplit = seedSplit.lstrip()
seedSplit = seedSplit.split()
for i in seedSplit:
    seedList.append(int(i))
inputList.pop(0)

maps = []
for i in inputList:
    mapList = []
    mapSplit = i.split(':')[1]
    mapSplit = mapSplit.lstrip()
    mapSplit = mapSplit.split()
    for j in range(0, len(mapSplit), 3):
        mapLine = []
        mapLine.append(int(mapSplit[j]))
        mapLine.append(int(mapSplit[j+1]))
        mapLine.append(int(mapSplit[j+2]))
        mapList.append(mapLine)
    maps.append(mapList)

for map in maps:
    modList = []
    for i in range(len(seedList)):
        seed = seedList[i]
        changed = False
        for mapLine in map:
            dRange = mapLine[0]
            sRange = mapLine[1]
            rangeNum = mapLine[2]
            if seed >= sRange and seed < sRange+rangeNum:
                modList.append(dRange + (seed-sRange))
                changed = True
        if not changed:
            modList.append(seed)
    seedList = modList.copy()

print(min(seedList))
            
        
