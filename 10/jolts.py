import itertools

with open('input.txt') as f:
    l = sorted(list(map(int, f.readlines())))
    l2 = [0] + l + [l[-1] + 3]
    diffs = [j-i for i, j in zip(l2[:-1], l2[1:])]
    print(diffs.count(1) * diffs.count(3)) # part 1

    x = [1] + [0] * l2[-1]
    for i in l2:
        for j in range(1, 4):
            if i - j in l2:
                x[i] += x[i-j]
    print(x[-1]) # part2
