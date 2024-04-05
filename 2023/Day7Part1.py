cardOrder = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
inputList = []
while True:
   line = input()
   if line == "'+":
       break
   else:
       inputList.append(line)

def findOrder(fullHand):
    trips = False
    pair1 = False
    pair2 = False
    for i in cardOrder:
        cardCount = fullHand['hand'].count(i)
        if cardCount == 5: return 6
        if cardCount == 4: return 5
        if cardCount == 3: trips = True
        if cardCount == 2:
            if pair1: pair2 = True
            else: pair1 = True
    if trips and pair1: return 4
    elif trips: return 3
    elif pair1 and pair2: return 2
    elif pair1: return 1
    return 0

def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j]['order'] > arr[j+1]['order']:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
            elif arr[j]['order'] == arr[j+1]['order']:
                for k in range(len(arr[j]['hand'])):
                    hand1 = arr[j]['hand']
                    hand2 = arr[j+1]['hand']
                    if cardOrder.index(arr[j]['hand'][k]) > cardOrder.index(arr[j+1]['hand'][k]):
                        arr[j], arr[j+1] = arr[j+1], arr[j]
                        swapped = True
                        break
                    elif cardOrder.index(arr[j]['hand'][k]) != cardOrder.index(arr[j+1]['hand'][k]):
                        break
        if not swapped:
            break

hands = []
for i in inputList:
    splitHand = i.split()
    fullHand = {'hand': list(splitHand[0]), 'bid': int(splitHand[1])}
    fullHand['order'] = findOrder(fullHand)
    hands.append(fullHand)
bubble_sort(hands)
sum = 0
for i in hands:
    sum += i['bid']*(hands.index(i)+1)

print(sum)