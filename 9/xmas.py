import itertools

def find_sum(l, result):
    return [(i, j) for i, j in itertools.combinations(l, 2) if i + j == result]

def find_contiguous_sum(l, result):
    return [l[i:j] for i in range(len(l)) for j in range(i, len(l)) if sum(l[i:j]) == result]

with open('input.txt', 'r') as f:
    l = list(map(int, f.readlines()))
    for i in range(25, len(l)):
        if len(find_sum(l[i-25:i], l[i])) == 0:
            print(l[i]) # part1
            part2 = find_contiguous_sum(l[:i], l[i])
            if len(part2) > 0:
                print(min(part2[0]) + max(part2[0]))
