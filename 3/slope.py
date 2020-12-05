import operator

def new_pos(pos, slope, right_limit):
    new_pos = list(map(operator.add, pos, slope))
    return (new_pos[0], new_pos[1] % right_limit)

with open("input.txt", 'r') as f:
    map_ = list(map(str.strip, f.readlines()))
    result = 1
    for slope in [(1, 1), (1, 3), (1, 5), (1, 7), (2, 1)]:
        begin = (0, 0)
        pos = new_pos(begin, slope, len(map_[0])-1)
        trees = 0
        while pos[0] < len(map_):
            if map_[pos[0]][pos[1]] == '#':
                trees +=1
            pos = new_pos(pos, slope, len(map_[0]))
        result *= trees
    print(result)
