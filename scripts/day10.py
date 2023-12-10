import sys

data = sys.stdin.read().strip().split("\n")
n = len(data)
m = len(data[0])

for i in range(n):
    if "S" in data[i]:
        start = (i, data[i].index("S"))
        break

#x -> y v
directions = {"-":((0, 1), (0, -1)), 
                "|":((1, 0), (-1, 0)), 
                "7":((0, -1), (1, 0)), 
                "J":((0, -1), (-1, 0)), 
                "L":((0, 1), (-1, 0)), 
                "F":((0, 1), (1, 0)), 
                "S":None ,".":None}


def reverse_dir(direction):
    return (-direction[0], -direction[1])

valid_dirs = dict()

for key, val in directions.items():
    if val:
        d1, d2 = val
        s1 = ""
        s2 = ""
        for k, v in directions.items():
            if v:
                if reverse_dir(d1) in v:
                    s1 += k
                if reverse_dir(d2) in v:
                    s2 += k
        valid_dirs[(key, d1)] = s1
        valid_dirs[(key, d2)] = s2
        

def next(position, direction):
    x, y = position
    i, j = direction
    if 0 <= x + i <= m and 0 <= y + j <= n:
        return data[x + i][y + j], (x + i, y + j)

def next_step(position, pipe, came_from):
    if directions[pipe]:
        dir1, dir2 = directions[pipe]
        if next(position, dir1)[1] == came_from:
            return next(position, dir2)
        else:
            return next(position, dir1)

def step_valid(position, direction, came_from):
    x, y = position
    return next_step(position, data[x][y], came_from)[0] in valid_dirs[(data[x][y], direction)]

def cycle(pos1, came_from):
    c = 1
    path = [came_from, pos1]
    x, y = pos1
    pipe, pos = next_step(pos1, data[x][y], came_from)
    a, b = pos
    while pipe != "S":
        if  not (step_valid(pos1, (a - x, b - y), came_from)):
            break
        came_from = pos1
        pos1 = pos
        pipe, pos = next_step(pos1, pipe, came_from)
        x, y = pos1
        a, b = pos
        path.append(pos1)
        c += 1
    else:
        return c, path

l, path_lst = cycle(next(start, (1, 0))[1], start)
print(l // 2 + 1)
path = set(path_lst)

all_pos = set()
for i in range(n):
    for j in range(m):
        if (i, j) not in path:
            all_pos.add((i, j))

# inside = set()
# outside = set()

# ds = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
# while all_pos:
#     connected = set()
#     ins = True
#     for p in all_pos:
#         pos = p
#         break
#     connected.add(pos)
#     all_pos.discard(pos)
#     stack = [pos]
#     while stack:
#         v = stack.pop()
#         for d in ds:
#             i, j = d
#             x, y = v
#             if 0 <= x + i <= m and 0 <= y + j <= n:
#                 if (x + i, y + j) in all_pos:
#                     connected.add((x + i, y + j))
#                     all_pos.discard((x + i, y + j))
#                     stack.append((x + i, y + j))
#             else:
#                 ins = False
#     if ins:
#         inside = inside.union(connected)
#     else:
#         outside = outside.union(connected)

# print(len(inside))

# string = ""
# for i in range(n):
#     for j in range(m):
#         if (i, j) in path:
#             string += "-"
#         elif (i, j) in outside:
#             string += "O"
#         elif (i, j) in inside:
#             string += "I"
#     string += "\n"

#print(string)
print(len(all_pos))
inside = set()
outside = set()
for k in range(len(path_lst)):
    x, y = path_lst[k]
    pipe = data[x][y]
    if pipe != "S":
        a, b = path_lst[k -1]
    else:
        a, b = path_lst[-1]
    direction = (x - a, y - b)
    left_on_up = None
    left_on_up2 = None
    if direction == (1, 0):
        left_on = (x, y + 1)
        right_on = (x, y - 1)
        if pipe == "J":
            left_on_up = (x + 1, y + 1)
            left_on_up2 = (x + 1, y)
    elif direction == (-1, 0):
        left_on = (x, y - 1)
        right_on = (x, y + 1)
        if pipe == "F":
            left_on_up = (x - 1, y - 1)
            left_on_up2 = (x - 1, y)
    elif direction == (0, 1):
        left_on = (x - 1, y)
        right_on = (x + 1, y)
        if pipe == "7":
            left_on_up = (x - 1, y + 1)
            left_on_up2 = (x, y + 1)
    else:
        left_on = (x + 1, y)
        right_on = (x - 1, y)
        if pipe == "L":
            left_on_up = (x + 1, y - 1)
            left_on_up2  = (x, y - 1)
    if 0 <= left_on[0] <= n and 0 <= left_on[1] <= m and left_on not in path:
        inside.add(left_on)
        all_pos.discard(left_on)
    if left_on_up and 0 <= left_on_up[0] <= n and 0 <= left_on_up[1] <= m and left_on_up not in path:
        inside.add(left_on_up)
        all_pos.discard(left_on_up)
    if left_on_up2 and 0 <= left_on_up2[0] <= n and 0 <= left_on_up2[1] <= m and left_on_up2 not in path:
        inside.add(left_on_up2)
        all_pos.discard(left_on_up2)
    # if 0 <= right_on[0] <= n and 0 <= right_on[1] <= m and right_on not in path:
    #     outside.add(right_on)
    #     all_pos.discard(right_on)


ds = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
stack = list(inside)
while stack:
    v = stack.pop()
    for d in ds:
        i, j = d
        x, y = v
        if 0 <= x + i <= m and 0 <= y + j <= n: 
            if (x + i, y + j) in all_pos:
                if data[x + i][y + j] != "+":
                    inside.add((x + i, y + j))
                    stack.append((x + i, y + j))
                    all_pos.discard((x+i, y+j))

# outside = set()
# for k in range(len(path_lst)):
#     x, y = path_lst[k]
#     pipe = data[x][y]
#     if k != len(path_lst) - 1:
#         a, b = path_lst[k +1]
#     else:
#         a, b = path_lst[0]
#     direction = (x - a, y - b)
#     left_on_up = None
#     if direction == (1, 0):
#         left_on = (x, y + 1)
#         if pipe == "J":
#             left_on_up = (x + 1, y + 1)
#     elif direction == (-1, 0):
#         left_on = (x, y - 1)
#         if pipe == "F":
#             left_on_up = (x - 1, y - 1)
#     elif direction == (0, 1):
#         left_on = (x - 1, y)
#         if pipe == "7":
#             left_on_up = (x - 1, y + 1)
#     else:
#         left_on = (x + 1, y)
#         if pipe == "L":
#             left_on_up = (x + 1, y - 1)
#     if 0 <= left_on[0] <= n and 0 <= left_on[1] <= m and left_on not in path:
#         outside.add(left_on)
#         all_pos.discard(left_on)
#     if left_on_up and 0 <= left_on_up[0] <= n and 0 <= left_on_up[1] <= m and left_on_up not in path:
#         outside.add(left_on_up)
#         all_pos.discard(left_on_up)


# ds = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (-1, -1), (-1, 1), (1, -1)]
# stack = list(outside)
# while stack:
#     v = stack.pop()
#     for d in ds:
#         i, j = d
#         x, y = v
#         if 0 <= x + i <= m and 0 <= y + j <= n: 
#             if (x + i, y + j) in all_pos:
#                 if data[x + i][y + j] != "+":
#                     outside.add((x + i, y + j))
#                     stack.append((x + i, y + j))
#                     all_pos.discard((x+i, y+j))

print(len(inside))
# for i in all_pos:
#     print(i)

string = ""
# for i in range(n):
#     for j in range(m):
#         if (i, j) in path:
#             string += data[i][j]
#         elif (i, j) in inside:
#             string += "I"
#         elif (i, j) in outside:
#             string += "O"
#         else:
#             string += "8"
#     string += "\n"

# print(string)
