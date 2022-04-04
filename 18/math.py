with open('input.txt', 'r') as f:
    ops = list(map(str.strip, f.readlines()))
    ops = [op.replace('(', '( ') for op in ops]
    ops = [op.replace(')', ' )') for op in ops]
    ops = [op.split() for op in ops]

def suffix(op):
    stack = []
    operator = None
    i = 0
    while i < len(op):
        if op[i].isdigit():
            stack.append(int(op[i]))
            if operator:
                stack.append(operator)
                operator = None
        elif op[i] == '(':
            stack.append(suffix(op[i+1:]))
            i = len(op[:i+1]) + op[i+1:].index(')')
            if operator:
                stack.append(operator)
                operator = None
        elif op[i] == ')':
            return stack
        elif op[i] in ('+', '-', '*', '/'):
            operator = op[i]
        i += 1
    return stack

def eval(expr):
    stack = []
    for el in expr:
        if el.isdigit():
            stack.append(wl)
        else:
            if t == '*':
                stack.append(stack.pop() * stack.pop())
            elif t == '+':
                stack.append(stack.pop() + stack.pop())
            else:
                raise ValueError('Undefined operator: %s' % t)
    return stack.pop()

print(ops[0])
print(suffix(ops[0]))
print(ops[1])
print(suffix(ops[1]))
