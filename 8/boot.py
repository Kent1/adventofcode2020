def isFinite(ops):
    l = [0] * len(ops)
    i = 0
    acc = 0
    while i < len(ops) and l[i] == 0:
        l[i] += 1
        if ops[i][0] == "acc":
            acc += ops[i][1]
            i += 1
        elif ops[i][0] == "jmp":
            i += ops[i][1]
        elif ops[i][0] == "nop":
            i += 1
    return i == len(ops), acc

def switch_instructions(i:int, ops):
    ops2 = ops[:]
    if ops2[i][0] == "nop":
        ops2[i] = ("jmp", ops2[i][1])
    elif ops2[i][0] == "jmp":
        ops2[i] = ("nop", ops2[i][1])
    return ops2

with open('input.txt', 'r') as f:
    input = map(str.split, f.readlines())
    ops = [(op, int(number)) for op, number in input]
    print(isFinite(ops)[1])
    for i in range(len(ops)):
        ops2 = switch_instructions(i, ops)
        result = isFinite(ops2)
        if result[0]:
            print(result[1])
        

