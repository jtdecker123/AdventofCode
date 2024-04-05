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
for i in inputList:
    listSet = list(i)
    length = len(listSet)
    middle_index = length // 2
    first_half = listSet[:middle_index]
    second_half = listSet[middle_index:]
    for j in first_half:
        if j in second_half:
            sum += priority(j)
            print(j)
            break
print(sum)