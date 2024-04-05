def process_seeds(seeds, mappings):
    seed_to_soil = {}
    for start, length in zip(seeds[::2], seeds[1::2]):
        for j in range(length):
            seed_to_soil[start + j] = start + j

    for mapping in mappings:
        mod_dict = {}
        for seed, soil in seed_to_soil.items():
            changed = False
            for dest_range, src_range, range_length in mapping:
                if src_range <= soil < src_range + range_length:
                    mod_dict[seed] = dest_range + (soil - src_range)
                    changed = True
                    break
            if not changed:
                mod_dict[seed] = soil
        seed_to_soil = mod_dict

    return min(seed_to_soil.values())

input_list = []
full_line = ''
while True:
    line = input()
    if line == "'+":
        input_list.append(full_line)
        break
    if not line:
        input_list.append(full_line)
        full_line = ''
    else:
        full_line += ' ' + line.lstrip()

seed_list = list(map(int, input_list[0].split(':')[1].lstrip().split()))
input_list.pop(0)

maps = []
for i in input_list:
    map_list = []
    map_split = i.split(':')[1].lstrip().split()
    map_list = [[int(map_split[j]), int(map_split[j+1]), int(map_split[j+2])] for j in range(0, len(map_split), 3)]
    maps.append(map_list)

result = process_seeds(seed_list, maps)
print(result)

'''
inputList = []
fullLine = ''
while True:
    line = input()
    if line == "'+":
        inputList.append(fullLine)
        break
    if not line:
        inputList.append(fullLine)
        fullLine = ''
    else: 
        fullLine += ' ' + line.lstrip()

seedList = list(map(int, inputList[0].split(':')[1].lstrip().split()))
fullSeedList = [start + j for start, numRange in zip(seedList[::2], seedList[1::2]) for j in range(numRange)]
inputList.pop(0)

maps = []
for i in inputList:
    mapList = []
    mapSplit = i.split(':')[1].lstrip().split()
    mapList = [[int(mapSplit[j]), int(mapSplit[j+1]), int(mapSplit[j+2])] for j in range(0, len(mapSplit), 3)]
    maps.append(mapList)

for single_map in maps:
    modSet = set()
    for seed in fullSeedList:
        for dRange, sRange, rangeNum in single_map:
            if sRange <= seed < sRange + rangeNum:
                modSet.add(dRange + (seed - sRange))
                break
        else:
            modSet.add(seed)
    fullSeedList = list(modSet)

print(min(fullSeedList))
'''