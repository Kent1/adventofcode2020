from functools import reduce
# Copied from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def chinese_remainder(n, a):
    sum = 0
    prod = reduce(lambda a, b: a*b, n)
    for n_i, a_i in zip(n, a):
        p = prod // n_i
        sum += a_i * mul_inv(p, n_i) * p
    return sum % prod

# Copied from https://rosettacode.org/wiki/Chinese_remainder_theorem#Python_3.6
def mul_inv(a, b):
    b0 = b
    x0, x1 = 0, 1
    if b == 1: return 1
    while a > 1:
        q = a // b
        a, b = b, a%b
        x0, x1 = x1 - q * x0, x0
    if x1 < 0: x1 += b0
    return x1

with open('input.txt', 'r') as f:
    file = f.readlines()
    t = int(file[0])
    ids = [int(x) for x in file[1].strip().split(',') if x != 'x']
    timestamps = ids[:]
    while not all([timestamp > t for timestamp in timestamps]):
        timestamps = [timestamp + id if timestamp < t else timestamp for timestamp, id in zip(timestamps, ids)]
    timestamp = min(timestamps)
    id = ids[timestamps.index(timestamp)]
    print(id * (timestamp - t))

    # part 2
    # Bruteforcing
    # ids = [int(x) if x != 'x' else 1 for x in file[1].strip().split(',')]
    # timestamps = ids[:]
    # print(ids)
    # i = 0
    # while not all([timestamps[i-1] + 1 == timestamps[i] for i in range(1, len(timestamps))]):
    #     i += 1
    #     if all([timestamps[i-1] < timestamps[i] for i in range(1, len(timestamps))]):
    #         timestamps[0] += timestamps[-1] // timestamps[0] * ids[0]
    #     else:
    #         print(timestamps)
    #     for i in range(1, len(timestamps)):
    #         while timestamps[i] <= timestamps[i-1]:
    #             timestamps[i] = timestamps[i] + timestamps[i-1]//timestamps[i] * ids[i]
    # print(timestamps)

    # Diophantine
    ids = [(x, int(y)) if y != 'x' else (x, 1) for (x, y) in enumerate(file[1].strip().split(','))]

    n = []
    a = []
    for pos, id in ids:
        n += [id]
        a += [-pos]
    print(chinese_remainder(n, a))
