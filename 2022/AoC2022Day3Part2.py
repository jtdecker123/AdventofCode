alphebetList = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
def priority(letter):
    for i in range(len(alphebetList)):
        if letter == alphebetList[i]:
            return i+1
inputList = []
while True:
   line = input()
   if line == "'+":
       break
   else:
       inputList.append(line)
sum = 0
index = 0
while index < len(inputList):
    listSet1 = list(inputList[index])
    listSet2 = list(inputList[index+1])
    listSet3 = list(inputList[index+2])
    for j in listSet1:
        if j in listSet2:
            if j in listSet3:
                sum += priority(j)
                print(j)
                break
    index += 3
print(sum)