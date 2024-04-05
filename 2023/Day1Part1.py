inputList = []
calTotal = 0
while True:
   line = input()
   if line == "'+":
       break
   else:
       inputList.append(line)
for i in inputList:
    myLine = list(i)
    newLine = []
    for j in myLine:
        if not j.isalpha():
            newLine.append(j)
    num = 10*int(newLine[0]) + int(newLine[-1])
    #print(num)
    calTotal += (num)

print(calTotal)