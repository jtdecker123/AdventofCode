inputList = []
while True:
   line = input()
   if line == "'+":
       break
   else:
       inputList.append(line)
signal = list(inputList[0])
set = []
processed = 0
for i in signal:
    flag = True
    if len(set) < 3:
        set.append(i)
        processed += 1
        continue
    set.append(i)
    processed += 1
    for j in set:
        if set.count(j)>1:
            flag = False
            break
    if flag:
        print(processed)
        print(set)
        break
    del set[0]
        