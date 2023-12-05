import sys
import time

data = sys.stdin.read().strip().split("\n")

def read_nums_from_line(x):
    nums = []
    j = 0
    while j < len(x):
        if x[j].isdigit():
            num = ""
            while j < len(x) and x[j].isdigit():
                num += x[j]
                j += 1
            nums.append(int(num))
        else:
            j += 1
    return nums

seeds = read_nums_from_line(data[0])
maps = []

j = -1
for i in range (1, len(data)):
    if data[i] == "":
        maps.append([])
        j += 1
    elif data[i][0].isdigit():
        maps[j].append(read_nums_from_line(data[i]))

locations = []
for seed in seeds:
    for m in maps:
        for l in m:
            if l[1] <= seed < l[1] + l[2]:
                seed = l[0] + seed - l[1]
                break
    locations.append(seed)

print(min(locations))

seeds2 = []
for i in range(int(len(seeds)/2)):
    s = [seeds[2 * i], seeds[2 * i] + seeds[2 * i + 1]]
    seeds2.append(s)

for m in maps:
    mapped_seeds = []
    while seeds2:
        seed = seeds2.pop()
        for l in m:
            low = l[1]
            high = l[1] + l[2]
            if low <= seed[0] < high:
                if low <= seed[1] < high:
                    new_seed = [l[0] + seed[0] - l[1], l[0] + seed[1] - l[1]]
                    mapped_seeds.append(new_seed)
                    break
                else:
                    new_seed = [l[0] + seed[0] - l[1], l[0] + l[2]]
                    new_seed2 = [high, seed[1]]
                    mapped_seeds.append(new_seed)
                    seeds2.append(new_seed2)
                    break
            elif seed[0] < low:
                if low < seed[1] < high:
                    new_seed = [l[0], l[0] + seed[1] - l[1]]
                    new_seed2 = [seed[0], low]
                    mapped_seeds.append(new_seed)
                    seeds2.append(new_seed2)
                    break
                elif high <= seed[1]:
                    new_seed = [l[0], l[0] + l[2]]
                    new_seed2 = [seed[0], low]
                    new_seed3 = [high, seed[1]]
                    mapped_seeds.append(new_seed)
                    seeds2.append(new_seed2)
                    seeds2.append(new_seed3)
                    break
        else:
            mapped_seeds.append(seed)
    seeds2 = mapped_seeds.copy()

lowest = float("inf")
for seed in seeds2:
    c = seed[0]
    if c < lowest:
        lowest = c

print(lowest)