inputList = []
while True:
   line = input()
   if line == "'+":
       break
   else:
       inputList.append(line)
def result(opp, you):
    score = 0
    val = 0
    if you == "X":
        score = 0
    if you == "Y":
        score = 3
    if you == "Z":
        score = 6
    if opp == "A":
        if you == "X":
            val = 3
        elif you == "Y":
            val = 1
        elif you == "Z":
            val = 2
    if opp == "B":
        if you == "X":
            val = 1
        elif you == "Y":
            val = 2
        elif you == "Z":
            val = 3
    if opp == "C":
        if you == "X":
            val = 2
        elif you == "Y":
            val = 3
        elif you == "Z":
            val = 1
    return [val,score]

sum = 0
for i in inputList:
    list(i)
    res = result(i[0],i[2])
    sum += res[0]
    sum += res[1]
print(sum)
