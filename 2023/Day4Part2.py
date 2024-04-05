import re

inputList = []
while True:
   line = input()
   if line == "'+":
       break
   else:
       inputList.append(line)

def getCount(card):
    count = 0
    for j in card[1]:
        if j in card[0]:
            count+=1
    return count

cards = []
for i in inputList:
    myLine = re.split(r'[:|]',i)
    winNums = myLine[1].strip()
    winInts = [int(num) for num in winNums.split()]
    myNums = myLine[2].strip()
    myInts = [int(num) for num in myNums.split()]
    card = {'cardNum': inputList.index(i), 'amount': 1, 'vals': [winInts, myInts]}
    count = getCount(card['vals'])
    card['score'] = count
    cards.append(card)

for i in range(len(cards)):
    counter = cards[i]['score']
    while counter > 0:
        cards[i+counter]['amount'] += cards[i]['amount']
        counter -= 1
total = 0
for i in cards:
    total+= i['amount']
print(total)