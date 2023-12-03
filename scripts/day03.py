import sys

data = sys.stdin.read().strip().split("\n")

def neighbours(i, start, end):
    lst = []
    for j in range(start-1, end+1):
        lst.append((i+1, j))
        lst.append((i-1, j))
    lst.append((i, start-1))
    lst.append((i, end))
    return lst

s = 0
d = dict()

for i in range(len(data)):
    j = 0
    while j < len(data[i]):
        if data[i][j].isdigit():
            start = j
            num = ""
            while j < len(data[i]) and data[i][j].isdigit():
                num += data[i][j]
                j += 1
            end = j
            num = int(num)
            flag = True
            for k, l in neighbours(i, start, end):
                if 0 <= k < len(data) and 0 <= l < len(data[0]) and data[k][l] != ".":
                    if flag:
                        s += num
                        flag = False
                    if (k, l) in d:
                        d[(k, l)].append(num)
                    else:
                        d[(k, l)] = [num]
        else:
            j += 1

print(s)

#part 2

s2 = 0

for key in d.keys():
    if len(d[key]) == 2:
        s2 += d[key][0] * d[key][1]

print(s2)

