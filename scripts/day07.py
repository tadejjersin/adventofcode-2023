import sys
import time

data = sys.stdin.read().strip().split("\n")

data = list(map(lambda x: x.split(" "), data))

cards = "23456789TJQKA"

def primary_strength(card):
    counter = [0 for _ in range(len(cards))]
    for i in card:
        counter[cards.index(i)] += 1
    
    if 5 in counter:
        return 38
    elif 4 in counter:
        return 37
    elif 3 in counter and 2 in counter:
        return 36
    elif 3 in counter:
        return 35
    elif counter.count(2) == 2:
        return 34
    elif 2 in counter:
        return 33
    else:
        return 32

def secondary_strength(card):
    s = ""
    for i in card:
        s+= chr(32 + cards.index(i))
    return s

def strength(card):
    return chr(primary_strength(card)) + secondary_strength(card)

data.sort(key=lambda x: strength(x[0]))

s = 0
for i in range(len(data)):
    s += (i+1) * int(data[i][1])

print(s)

cards2 = "J23456789TQKA"

def secondary_strength2(card):
    s = ""
    for i in card:
        s+= chr(32 + cards2.index(i))
    return s

def primary_strength2(card):
    counter = [0 for _ in range(len(cards))]
    for i in card:
        counter[cards2.index(i)] += 1
    
    r = counter[0]
    
    if (5 - r) in counter[1:]:
        return 39
    elif (4 - r) in counter[1:]:
        return 38
    elif (r == 0 and 3 in counter[1:] and 2 in counter[1:]) or (r == 1 and counter[1:].count(2) == 2):
        return 37
    elif (3 - r) in counter[1:]:
        return 36
    elif r == 0 and counter[1:].count(2) == 2:
        return 35
    elif (2 - r) in counter[1:]:
        return 34
    else:
        return 32

def strength2(card):
    return chr(primary_strength2(card)) + secondary_strength2(card)

data.sort(key=lambda x: strength2(x[0]))

s2 = 0
for i in range(len(data)):
    s2 += (i+1) * int(data[i][1])

print(s2)