
d = {
    'B': '1',
    'F': '0',
    'R': '1',
    'L': '0',
}

def seatId(boardpass):
    for char in d:
        boardpass = boardpass.replace(char, d[char])
    return int(boardpass, 2)

with open("input.txt", 'r') as f:
    l = f.readlines()
    seats = [seatId(boardpass) for boardpass in l]
    print(max(seats)) # part 1
    seats = sorted(seats)
    for i in range(1, len(seats)):
        if seats[i] != seats[i-1] + 1:
            print(seats[i]-1) # part 2
