import sys

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

times = read_nums_from_line(data[0])
distances = read_nums_from_line(data[1])

time2 = ""
for t in times:
    time2 += str(t)
time2 = int(time2)
times.append(time2)

distance2 = ""
for d in distances:
    distance2 += str(d)
distance2 = int(distance2)
distances.append(distance2)

margin2 = 0

prod = 1
for i in range(len(times)):
    # (T - t) * t = d => t ** 2 - T * t + d = 0
    d = distances[i]
    T = times[i]
    D = (T ** 2 - 4 * d) ** (0.5)
    lowest = (T - D) / 2
    highest = (T + D) / 2
    margin = int(highest) - int(lowest) 
    margin = margin - 1 if int(highest) == highest else margin
    if i == len(times) - 1:
        margin2 = margin
    else:
        prod *= margin

print(prod)
print(margin2)