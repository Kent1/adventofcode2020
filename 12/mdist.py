import math 

def move_ship(pos, d, v):
    if d in ('R', 'L'):
        angle = v if d == 'R' else -v 
        return (pos[0] + angle, pos[1], pos[2])
    elif d == 'F':
        return (pos[0], int(math.cos(math.radians(pos[0]))) * v + pos[1], int(math.sin(math.radians(pos[0]))) * v + pos[2])
    else:
        a = 0
        b = 0
        if d == 'N':
            a = v
        elif d == 'S':
            a = -v
        elif d == 'W':
            b = -v
        elif d == 'E':
            b = v
        return (pos[0], pos[1] + a, pos[2] + b)

def move_ship2(pos, d, v, waypoint):
    if d in ('R', 'L'):
        angle = math.radians(v if d == 'R' else -v)
        return pos, (int(math.cos(angle)) * (waypoint[0]) - int(math.sin(angle)) * (waypoint[1]),
                     int(math.sin(angle)) * (waypoint[0]) + int(math.cos(angle)) * (waypoint[1]))
    elif d == 'F':
        return (v * waypoint[0] + pos[0], v * waypoint[1] + pos[1]), waypoint
    else:
        a = 0
        b = 0
        if d == 'N':
            a = v
        elif d == 'S':
            a = -v
        elif d == 'W':
            b = -v
        elif d == 'E':
            b = v
        return pos, (waypoint[0] + a, waypoint[1] + b)


with open('input.txt', 'r') as f:
    l = [(line[0:1], int(line[1:])) for line in f.readlines()]
    # Part 1
    ship = (90, 0, 0)
    for d, v in l:
        ship = move_ship(ship, d, v)
    print(int(math.fabs(ship[1]) + math.fabs(ship[2])))
    # Part 2
    ship = (0, 0)
    waypoint = (1, 10)
    for d, v in l:
        ship, waypoint = move_ship2(ship, d, v, waypoint)
    print(int(math.fabs(ship[0]) + math.fabs(ship[1])))