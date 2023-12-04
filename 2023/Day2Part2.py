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
    fullGame = []
    for j in sets:
        game = {'red': 0, 'green': 0, 'blue': 0}
        for k in range(1, len(j),2):
            game[j[k]] += j[k-1]
        fullGame.append(game)
    minR = fullGame[0]['red']
    minG = fullGame[0]['green']
    minB = fullGame[0]['blue']

    for j in range(1,len(fullGame)):
        if fullGame[j]['red'] > minR:
            minR = fullGame[j]['red']
        if fullGame[j]['green'] > minG:
            minG = fullGame[j]['green']
        if fullGame[j]['blue'] > minB:
            minB = fullGame[j]['blue']
    
    sum+= (minR*minG*minB)

print(sum)
