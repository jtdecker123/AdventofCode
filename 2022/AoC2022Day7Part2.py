biggestDirectory = 0
deletedDir = 70000000

inputList = []
while True:
   line = input()
   if line == "'++'":
       break
   else:
       inputList.append(line)

def getConstraints(beginSearch):
    iLI = beginSearch
    ls = False
    startLS = 0
    endLS = 0
    while iLI < len(inputList):
        item = inputList[iLI]
        if item == '$ ls':
            startLS = iLI
            ls = True
        if '$' in item and item != '$ ls':
            endLS = iLI
        if startLS < endLS and ls:
            return [startLS,endLS]
        iLI +=1
    return [startLS,len(inputList)]

max = 0
def createDirectorySet(start, end):
    global max
    global sizeTotal
    if end > max:
        max = end
    smallDirectory = dict()
    for i in range(start+1,end):
        inputSplit = inputList[i].split(' ')
        smallDirectory[(inputSplit[1])] = (inputSplit[0])
    for i in range(start+1,end):
        inputSplit = inputList[i].split(' ')
        if inputSplit[0] == 'dir':
            nextLS = getConstraints(max)
            smallDirectory[(inputSplit[1])] = createDirectorySet(nextLS[0],nextLS[1])
    return smallDirectory

def getLargestSize(dir):
    global biggestDirectory
    counter = 0
    for item in dir:
        if type(dir[item]) == dict:
            counter += getLargestSize(dir[item])
        else:
            counter += int(dir[item])
    if counter > biggestDirectory:
        biggestDirectory = counter
    return counter

def compareSize(dir):
    global sizeToDelete
    global deletedDir
    counter = 0
    for item in dir:
        if type(dir[item]) == dict:
            counter += compareSize(dir[item])
        else:
            counter += int(dir[item])
    if counter > sizeToDelete and counter < deletedDir:
        deletedDir = counter
    return counter

firstConstraint = getConstraints(0)
directory = createDirectorySet(firstConstraint[0],firstConstraint[1])
print(directory)
getLargestSize(directory)
sizeToDelete = biggestDirectory - (70000000-30000000)
compareSize(directory)
print(deletedDir)
