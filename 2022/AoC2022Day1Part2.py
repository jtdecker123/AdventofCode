inputList = []
calTotal1 = 0
calTotal2 = 0
calTotal3 = 0
holderCount1 = 0
holderCount2 = 0
runningTotal = 0
while True:
   line = input()
   if line == "'+":
       break
   else:
       inputList.append(line)
for i in inputList:
    if i == "":
        if runningTotal > calTotal1:
            holderCount1 = calTotal1
            holderCount2 = calTotal2
            calTotal1 = runningTotal
            calTotal2 = holderCount1
            calTotal3 = holderCount2
        elif runningTotal > calTotal2:
            holderCount2 = calTotal2
            calTotal2 = runningTotal
            calTotal3 = holderCount2
        elif runningTotal > calTotal3:
            calTotal3 = runningTotal
        runningTotal = 0
        continue
    runningTotal += int(i)
print(calTotal1+calTotal2+calTotal3)