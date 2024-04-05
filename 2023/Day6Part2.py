inputList = []
while True:
   line = input()
   if line == "'+":
       break
   else:
       inputList.append(line)
times = inputList[0].split(':')[1]
times = int(times.replace(" ", ""))

distances = inputList[1].split(':')[1]
distances = int(distances.replace(" ", ""))

total = 0
for j in range(times+1):
    speed = j
    time = times-j
    distance = speed*time
    if distance > distances:
        total+=1

print(total)