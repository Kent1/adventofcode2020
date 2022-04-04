with open('input.txt', 'r') as f:
    m = [list(line.strip()) for line in f.readlines()]
    m = { (i, j, 0) : y for i, x in enumerate(m) for j, y in enumerate(x) if y == '#'}

def neighbours_(pos):
    if len(pos)==1:
        return [(pos[0]-1,), (pos[0],), (pos[0]+1,)]
    n = neighbours_(pos[1:])
    return set([(pos[0], *i) for i in n] + \
           [(pos[0]+1, *i) for i in n] + \
           [(pos[0]-1, *i) for i in n])

def neighbours(pos):
    return neighbours_(pos) - {pos}

def get_infinity_map(positions):
    result = set()
    for pos in positions:
        result |= neighbours_   (pos)
    return result

def process(m):
    m2 = m.copy()
    for pos in get_infinity_map(m.keys()):
        active = sum([i in m for i in neighbours(pos)])
        if pos in m and not (2 <= active <= 3):
            del m2[pos]
        elif pos not in m and active == 3:
            m2[pos] = '#'
    return m2

print(m)
for _ in range(6):
    m = process(m)
print(len(m))

with open('input.txt', 'r') as f:
    m = [list(line.strip()) for line in f.readlines()]
    m = { (i, j, 0, 0) : y for i, x in enumerate(m) for j, y in enumerate(x) if y == '#'}

for _ in range(6):
    m = process(m)
print(len(m))
