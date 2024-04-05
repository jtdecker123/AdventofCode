stack = [['N', 'R', 'G', 'P'],['J', 'T', 'B', 'L', 'F', 'G', 'D', 'C'],['M', 'S', 'V'],['L', 'S', 'R', 'C', 'Z', 'P'],['P', 'S', 'L', 'V', 'C', 'W', 'D', 'Q'],['C', 'T', 'N', 'W', 'D', 'M', 'S'],['H', 'D', 'G', 'W', 'P'],['Z', 'L', 'P', 'H', 'S', 'C', 'M', 'V'],['R', 'P', 'F', 'L', 'W', 'G', 'Z']]
#stack = [['Z','N'],['M','C','D'],['P']]
def instruct(quantity,start,end):
    for i in range(quantity):
        stack[end-1].append(stack[start-1].pop(-1))
inputList = []
while True:
   line = input()
   if line == "'+":
       break
   else:
       inputList.append(line)
for i in inputList:
    list2 = i.split(" ")
    instruct(int(list2[1]),int(list2[3]),int(list2[5]))
for j in stack:
    print(j[-1])