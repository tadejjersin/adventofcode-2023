import sys

data = list(map(lambda x: list(map(int, x.split(" "))),sys.stdin.read().strip().split("\n")))

data2 = []
for lst in data:
    lst_copy = lst.copy()
    l = len(lst_copy)
    i = l
    while i > 1:
        for j in range(1, i):
            lst_copy[j - 1] = lst_copy[j] - lst_copy[j-1]
        i -= 1
    data2.append(lst_copy)

print(sum(map(sum, data2)))

s = 0
for lst in data:
    l = len(lst)
    i = l
    while i > 1:
        first = lst[0]
        for j in range(1, i):
            lst[j - 1] = lst[j] - lst[j-1]
        i -= 1
        lst[i] = first
    lst.reverse()
    while len(lst) > 1:
        x = lst.pop()
        y = lst.pop()
        lst.append(y - x)
    s += lst[0]

print(s) 
