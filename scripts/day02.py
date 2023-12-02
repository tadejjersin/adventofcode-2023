import sys

str_data = sys.stdin.read()
data = str_data.strip().split("\n")

s = 0

for x in data:
    i = 5
    gameid = ""
    while x[i].isdigit():
        gameid += x[i]
        i += 1
    flag = True
    j = i+1
    while j < len(x):
        if x[j].isdigit():
            num = ""
            while x[j].isdigit():
                num += x[j]
                j += 1
            num = int(num)
            if x[j + 1] == "b" and num > 14:
                flag = False
            elif x[j + 1] == "r" and num > 12:
                flag = False
            elif x[j + 1] == "g" and num > 13:
                flag = False
        else:
            j += 1
    if flag:
        s += int(gameid)

print(s)

s2 = 0

for x in data:
    i = 5
    while x[i].isdigit():
        i += 1
    j = i+1
    d = {"r": 0, "g":0, "b":0}
    while j < len(x):
        if x[j].isdigit():
            num = ""
            while x[j].isdigit():
                num += x[j]
                j += 1
            num = int(num)
            if d[x[j+1]] < num:
                d[x[j+1]] = num
        else:
            j += 1
    s2 += d["r"] * d["b"] * d["g"]

print(s2)