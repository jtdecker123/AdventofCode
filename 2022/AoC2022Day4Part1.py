inputList = []
while True:
   line = input()
   if line == "'+":
       break
   else:
       inputList.append(line)
sum = 0
for i in inputList:
    splitList = i.split(",")
    before = True
    set1 = splitList[0].split("-")
    set2 = splitList[-1].split("-")
    start1 = int(set1[0])
    start2 = int(set2[0])
    end1 = int(set1[-1])
    end2 = int(set2[-1])
    if start1 <= start2 and end1 >= end2:
        sum += 1
        print(i)
    elif start2 <= start1 and end2 >= end1:
        sum += 1
        print(i)
print(sum)

