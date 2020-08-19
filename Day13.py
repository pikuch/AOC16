
# load the data
with open("Day13input.txt") as f:
    data = int(f.read())

target_x = 31
target_y = 39

area = dict()

# testing data
# data = 10
# target_x = 7
# target_y = 4


def get_pos(x, y):
    if x < 0 or y < 0:
        return -2
    if (x, y) in area:
        return area[(x, y)]
    v = x * x + 3 * x + 2 * x * y + y + y * y + data
    bits = 0
    while v:
        bits += v % 2
        v //= 2
    area[(x, y)] = -(bits % 2) - 1
    return area[(x, y)]


def print_map(area):
    max_x = 0
    max_y = 0
    for room in area:
        if room[0] > max_x:
            max_x = room[0]
        if room[1] > max_y:
            max_y = room[1]
    for y in range(max_y + 2):
        for x in range(max_x + 2):
            if (x, y) in area:
                if area[(x, y)] == -1:
                    print("   ", end="")
                elif area[(x, y)] == -2:
                    print(" ██", end="")
                else:
                    print(f"{area[(x, y)]:3d}", end="")
            else:
                print(" ░░", end="")
        print("")


to_check = [(1, 1, 0)]
area[(1, 1)] = 0

while len(to_check):
    xx, yy, move = to_check.pop(0)
    if xx == target_x and yy == target_y:
        print_map(area)
        print(f"Found a {move} steps long path to {target_x}, {target_y}")
        break
    if get_pos(xx - 1, yy) == -1:
        area[(xx - 1, yy)] = move + 1
        to_check.append((xx - 1, yy, move + 1))
    if get_pos(xx + 1, yy) == -1:
        area[(xx + 1, yy)] = move + 1
        to_check.append((xx + 1, yy, move + 1))
    if get_pos(xx, yy - 1) == -1:
        area[(xx, yy - 1)] = move + 1
        to_check.append((xx, yy - 1, move + 1))
    if get_pos(xx, yy + 1) == -1:
        area[(xx, yy + 1)] = move + 1
        to_check.append((xx, yy + 1, move + 1))

count50 = 0
for a in area:
    if 0 <= area[a] <= 50:
        count50 += 1
print(f"{count50} locations can be reached within 50 steps")
