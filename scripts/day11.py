import sys

data = sys.stdin.read().strip().split("\n")

expanded_rows = []
for row in data:
    if "#" in row:
        expanded_rows.append(row)
    else:
        expanded_rows.append(row)
        expanded_rows.append(row)

expanded = ["" for _ in range(len(expanded_rows))]
for j in range(len(expanded_rows[0])):
    flag = True
    for i in range(len(expanded_rows)):
        if expanded_rows[i][j] == "#":
            flag = False
        expanded[i] += expanded_rows[i][j]
    if flag:
        for i in range(len(expanded_rows)):
            expanded[i] += expanded_rows[i][j]

galaxies = []
for i in range(len(expanded)):
    for j in range(len(expanded[0])):
        if expanded[i][j] == "#":
            galaxies.append((i, j))

s = 0
l = len(galaxies)
for i in range(l):
    for j in range(i+1, l):
        x1, y1 = galaxies[i]
        x2, y2 = galaxies[j]
        s += abs(x2 - x1) + abs(y2 - y1)

print(s)


expanded_rows = []
for i in range(len(data)):
    if "#" not in data[i]:
        expanded_rows.append(i)

expanded_cols = []
for j in range(len(data[0])):
    flag = True
    for i in range(len(data)):
        if data[i][j] == "#":
            flag = False
    if flag:
        expanded_cols.append(j)

print(expanded_rows)
print(expanded_cols)

galaxies = []
for i in range(len(data)):
    for j in range(len(data[0])):
        if data[i][j] == "#":
            galaxies.append((i, j))

s = 0
l = len(galaxies)
n = 999999
print(len(galaxies))
for i in range(l):
    for j in range(i+1, l):
        x1, y1 = galaxies[i]
        x2, y2 = galaxies[j]
        s += abs(x2 - x1) + abs(y2 - y1)
        for k in expanded_rows:
            if min(x1, x2) < k < max(x1, x2):
                s += n
        for m in expanded_cols:
            if min(y1, y2) < m < max(y1, y2):
                s += n


print(s)