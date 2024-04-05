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
for i in inputList:
    myLine = re.split(r'[:;]',i)
    gameID = myLine.pop(0)
    gameNum = int(gameID.split()[1])
    sets = []
    for j in myLine:
        firstSplit = j.split(',')
        trimmedList = [s.lstrip() for s in firstSplit]
        result = []
        for item in trimmedList:
            parts = item.split()  # Splitting each element by spaces
            for part in parts:
                if part.isdigit():  # Checking if the part is a digit
                    result.append(int(part))  # If it's a digit, convert to integer and add to the result
                else:
                    result.append(part)
        sets.append(result)
        #print(sets)
    valid = True
    minRed = -1
    minGreen = -1
    minBlue = -1
    for j in sets:
        game = {'red': 0, 'green': 0, 'blue': 0}
        for k in range(1, len(j),2):
            game[j[k]] += j[k-1]
        if game['red'] > 12 or game['green'] > 13 or game['blue'] > 14:
            valid = False
    if valid:
        sum+= gameNum

print(sum)
