import re

mask_p = r'mask = ([10X]{36})'
mem_p = r'mem\[(\d+)\] = (\d+)'

def masked(mask, n):
    return n & int(mask.replace('X', '1'), 2) | int(mask.replace('X', '0'), 2)

with open('input.txt', 'r') as f:
    l = list(map(str.strip, f.readlines()))

def part1():
    mem = {}
    mask = 'X' * 36
    for instruction in l:
        if (match := re.search(mask_p, instruction)):
            mask = match.group(1)
        elif (match := re.search(mem_p, instruction)):
            mem[int(match.group(1))] = masked(mask, int(match.group(2)))
        else:
            raise Exception()
    print(sum(mem.values()))

def get_addresses(mask, origin):
    addresses = ['']
    for i, char in enumerate(mask):
        if char == '0':
            addresses = [address + origin[i] for address in addresses]
        elif char == '1':
            addresses = [address + '1' for address in addresses]
        else:
            addresses = [address + '0' for address in addresses] + [address + '1' for address in addresses]
    return [int(address, 2) for address in addresses]

def part2():
    mem = {}
    mask = '0' * 36
    for instruction in l:
        if (match := re.search(mask_p, instruction)):
            mask = match.group(1)
        elif (match := re.search(mem_p, instruction)):
            for adress in get_addresses(mask, bin(int(match.group(1)))[2:].zfill(36)):
                mem[adress] = int(match.group(2))
        else:
            raise Exception()
    print(sum(mem.values()))

part1()
part2()