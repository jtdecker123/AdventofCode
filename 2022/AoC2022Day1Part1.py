inputList = []
calTotal = 0
runningTotal = 0
while True:
   line = input()
   if line == "'+":
       break
   else:
       inputList.append(line)
for i in inputList:
    if i == "":
        if runningTotal > calTotal:
            calTotal = runningTotal
        runningTotal = 0
        continue
    runningTotal += int(i)
print(calTotal)