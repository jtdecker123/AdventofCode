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
        val = 1
    if you == "Y":
        val = 2
    if you == "Z":
        val = 3
    if opp == "A":
        if you == "X":
            score = 3
        elif you == "Y":
            score = 6
        elif you == "Z":
            score = 0
    if opp == "B":
        if you == "X":
            score = 0
        elif you == "Y":
            score = 3
        elif you == "Z":
            score = 6
    if opp == "C":
        if you == "X":
            score = 6
        elif you == "Y":
            score = 0
        elif you == "Z":
            score = 3
    return [val,score]

sum = 0
for i in inputList:
    list(i)
    res = result(i[0],i[2])
    sum += res[0]
    sum += res[1]
print(sum)
