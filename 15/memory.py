import sys
start = [int(x) for x in sys.argv[1].split(',')]
d = {n: i+1 for i, n in enumerate(start[:-1])}
toAdd = start[-1]
for i in range(len(start), 2020):
    d[toAdd], toAdd = i, i - d.get(toAdd, i)
print(toAdd)