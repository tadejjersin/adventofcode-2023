import sys

data = sys.stdin.read().strip().split("\n")


instructions = data[0]

paths = dict()
for i in range(2,len(data)):
    point = data[i][:3]
    path = (data[i][7:10], data[i][12:15])
    paths[point] = path

start = "AAA"
end = "ZZZ"
l = len(instructions)
i = 0
while start != end:
    if instructions[i % l] == "L":
        start = paths[start][0]
    elif instructions[i % l] == "R":
        start = paths[start][1]
    i += 1

print(i)

starts = [point for point in paths.keys() if point[2] == "A"]
ends = []

for s in range(len(starts)):
    start = starts[s]
    j = 0
    while start[2] != "Z":
        if instructions[j % l] == "L":
            start = paths[start][0]
        elif instructions[j % l] == "R":
            start = paths[start][1]
        j += 1
    ends.append(j)

def gcd(x, y):
    if x == 0:
        return y
    else:
        return gcd(y % x, x)

def lcm(x, y):
    return (x * y) // gcd(x, y)

while len(ends) != 1:
    x = ends.pop()
    y = ends.pop()
    z = lcm(x, y)
    ends.append(z)

print(ends[0])