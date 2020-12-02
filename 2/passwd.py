def check_pwd(char, min, max, pwd):
    count = sum([char == i for i in pwd])
    return min <= count <= max

def check_pwd2(char, pos1, pos2, pwd):
    return (pwd[pos1-1] == char) != (pwd[pos2-1] == char)

with open("input.txt", 'r') as f:
    count1 = 0
    count2 = 0
    for line in f.readlines():
        rule, pwd = line.strip().split(": ")
        minmax, char = rule.split()
        min, max = map(int, minmax.split("-"))
        if check_pwd(char, min, max, pwd):
            count1+=1
        if check_pwd2(char, min, max, pwd):
            count2+=1
    print(count1)
    print(count2)
