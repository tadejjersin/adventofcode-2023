import sys

data = sys.stdin.read().strip().split("\n")

s = 0
card_counter = [1 for _ in range(len(data))]

for i in range(len(data)):
    winning_nums = []
    nums = []
    flag = True
    j = 9
    while j < len(data[i]):
        num = ""
        if data[i][j].isdigit():
            while j < len(data[i]) and data[i][j].isdigit():
                num += data[i][j]
                j += 1
            if flag:
                winning_nums.append(int(num))
            else:
                nums.append(int(num))
        elif data[i][j] == "|":
            flag = False
            j += 1
        else:
            j += 1
    c = 0
    for n in nums:
        if n in winning_nums:
            c += 1
    
    if c:
        s += 2**(c-1)
        for k in range(1, c + 1):
            if i + k < len(data):
                card_counter[i + k] += card_counter[i]

print(s)
print(sum(card_counter))