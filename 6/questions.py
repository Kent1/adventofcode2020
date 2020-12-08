with open("input.txt", 'r') as f:
    l = [x.split() for x in f.read().split("\n\n")]
    print(sum([len(set("".join(group))) for group in l])) # part 1
    print(sum([len(set(group[0]).intersection(*group)) for group in l])) # part 2
