def resplit(origLine):
    compList = ['one', '1', 'two', '2', 'three', '3', 'four', '4', 'five', '5', 'six', '6', 'seven', '7', 'eight', '8', 'nine', '9']
    newList = []
    for i in origLine:
        if i.isdigit():
            newList.append(i)
            continue
        for j in range(len(i)):
            for k in range(j,len(i)+1):
                currentSplice = i[j:k]
                if currentSplice in compList:
                    newList.append(compList[compList.index(currentSplice)+1])
                    break
    return newList

inputList = []
calTotal = 0
while True:
   line = input()
   if line == "'+":
       break
   else:
       inputList.append(line)
for i in inputList:
    newLine = []
    currentIndex = 0
    for j in range(len(i)):
        if not i[j].isalpha():
            if i[currentIndex:j] != '':
                newLine.append(i[currentIndex:j])
            if i[j] != '':
                newLine.append(i[j])
            currentIndex = j+1
    if currentIndex < len(i):
        newLine.append(i[currentIndex:])
    finalLine = resplit(newLine)
    num = 10*int(finalLine[0]) + int(finalLine[-1])
    #print(num)
    calTotal+=num
print(calTotal)