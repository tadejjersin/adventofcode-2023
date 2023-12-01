import sys

str_data = sys.stdin.read()
data = str_data.strip().split("\n")

def get_num(x):
    s=""
    for i in x:
        if i.isdigit():
            s += i
            break
    for i in x[::-1]:
        if i.isdigit():
            s += i
            break
    return int(s)
        

result1 = sum(list(map(lambda x: get_num(x), data)))
print(result1)

nums = {"one":1, "two":2, "three":3, "four":4, "five":5, "six":6, "seven":7, "eight":8, "nine":9}
def get_num2(x):
    s = ""
    l = len(x)
    for i in range(l):
        if x[i].isdigit():
            s += x[i]
            break
        else:
            for j in nums.keys():
                if i+len(j) <= l and x[i:i+len(j)] == j:
                    s += str(nums[j])
                    break
            if s:
                break
    for i in range(l)[::-1]:
        if x[i].isdigit():
            s += x[i]
            break
        else:
            for j in nums.keys():
                if i-len(j) + 1 >= 0 and x[i-len(j)+1:i+1] == j:
                    s += str(nums[j])
                    break
            if len(s) > 1:
                break
    return int(s)

result2 = sum(list(map(lambda x: get_num2(x), data)))
print(result2)

