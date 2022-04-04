import copy

def people_around(seats, i, j):
    def seat_taken(seats, i, j, k, l):
        # return 0 <= i < len(seats) and 0 <= j < len(seats[i]) and seats[i][j] == "#" # Part 1
        while 0 <= i < len(seats) and 0 <= j < len(seats[i]):
            if seats[i][j] == "#":
                return True
            elif seats[i][j] == "L":
                return False
            i += k
            j += l
        return False
    up = seat_taken(seats, i-1, j, -1, 0)
    down = seat_taken(seats, i+1, j, +1, 0)
    left = seat_taken(seats, i, j-1, 0, -1)
    right = seat_taken(seats, i, j+1, 0, +1)
    upleft = seat_taken(seats, i-1, j-1, -1, -1)
    upright = seat_taken(seats, i-1, j+1, -1, +1)
    downleft = seat_taken(seats, i+1, j-1, +1, -1)
    downright = seat_taken(seats, i+1, j+1, +1, +1)
    return up + down + left + right + upleft + upright + downleft + downright

def printl(l):
    [print(x) for x in l]
    print()

with open('input.txt', 'r') as f:
    input = list(map(str.strip, f.readlines()))
    seats = []
    for row in range(len(input)):
        seats.append([])
        seats[row][:0] = input[row]
    no_change = False
    count = 0
    printl(seats)
    while no_change == False:
        count += 1
        no_change = True
        seats2 = copy.deepcopy(seats) # copy to simulate simultaneous
        for row, line in enumerate(seats):
            for column, seat in enumerate(line):
                if seat == 'L' and people_around(seats, row, column) < 1:
                    seats2[row][column] = '#'
                    no_change = False
                if seat == '#' and people_around(seats, row, column) >= 5:
                    seats2[row][column] = 'L'
                    no_change = False
        seats = seats2
        printl(seats)
    print(sum([row.count("#") for row in seats]))
