from hashlib import md5

# load the data
with open("Day17input.txt") as f:
    passcode = f.read()

# test
#passcode = "hijkl"
#passcode = "ihgpwlah"
#passcode = "kglvqrro"
#passcode = "ulqzkmiv"


def get_open_doors(path, x, y):
    s = passcode + path
    hs = md5(s.encode()).hexdigest()
    answer = []
    if y > 0 and hs[0] > "a":  # UP
        answer.append((0, -1, "U"))
    if y < 3 and hs[1] > "a":  # DOWN
        answer.append((0, 1, "D"))
    if x > 0 and hs[2] > "a":  # LEFT
        answer.append((-1, 0, "L"))
    if x < 3 and hs[3] > "a":  # RIGHT
        answer.append((1, 0, "R"))
    return answer


def find_paths(to_check):
    shortest = 10**10
    shortest_path = ""
    longest = 0
    while len(to_check):
        x, y, path, moves = to_check.pop(0)
        if x == 3 and y == 3:
            if moves > longest:
                longest = moves
            if moves < shortest:
                shortest = moves
                shortest_path = path
            continue
        doors = get_open_doors(path, x, y)
        for dx, dy, newdir in doors:
            to_check.append((x + dx, y + dy, path + newdir, moves + 1))
    return shortest, shortest_path, longest


to_check = [(0, 0, "", 0)]  # position and path so far
shortest, shortest_path, longest = find_paths(to_check)
print(f"The shortest path is: {shortest_path} ({shortest}) and the longest is {longest} steps long")
