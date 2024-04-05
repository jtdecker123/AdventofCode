inputList = []
while True:
   line = input()
   if line == "'+":
       break
   else:
       inputList.append(line)
times = inputList[0].split()
times.pop(0)
times = [int(num) for num in times]

distances = inputList[1].split()
distances.pop(0)
distances = [int(num) for num in distances]

combos = []
for i in range(len(times)):
    combos.append(0)
    for j in range(times[i]+1):
        speed = j
        time = times[i]-j
        distance = speed*time
        if distance > distances[i]:
            combos[i]+=1

total = 1
for i in combos:
    total *= i

print(total)