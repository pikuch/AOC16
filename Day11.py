
# load the data
with open("Day11input.txt") as f:
    data = f.read().split("\n")

floors = []
for line in data:
    objects = line.split(",")
    floor = []
    for o in objects:
        parsed = o.split()
        if len(parsed):
            floor.append(parsed)
    floors.append(floor)

elements = []
for floor in floors:
    if not len(floor):
        continue
    for el in floor:
        if el[0] not in elements:
            elements.append(el[0])


def encode_string(floor_list):
    encoded = "1"  # elevator position
    for fl in floor_list:
        encoded += "."
        if not len(fl):
            continue
        for el in fl:
            if el[1] == "G":
                encoded += chr(ord("A") + elements.index(el[0]))
            else:
                encoded += chr(ord("a") + elements.index(el[0]))
    return encoded


def is_solution(state):
    items = state.split(".")
    if items[0] == "4":
        if items[1] == items[2] == items[3] == "":
            return True
    return False


def try_move(state):
    items = state.split(".")
    lvl = int(items[0])
    if lvl > 1:  # can move down
        # try moving one item
        for i in range(len(items[lvl])):
            items[lvl - 1] += items[lvl][i]
            items[lvl] = items[lvl][:i] + items[lvl][i+1:]
            items[0] = str(lvl - 1)
            yield ".".join(items)
        # try moving two items
        for i in range(len(items[lvl])):
            for j in range(i+1, len(items[lvl])):
                # TODO: check if can move items together
                items[lvl - 1] += items[lvl][i] + items[lvl][j]
                items[lvl] = items[lvl][:i] + items[lvl][i + 1:j] + items[lvl][j + 1:]
                items[0] = str(lvl - 1)
                yield ".".join(items)

    if lvl < 4:  # can move up
        # try moving one item
        for i in range(len(items[lvl])):
            items[lvl + 1] += items[lvl][i]
            items[lvl] = items[lvl][:i] + items[lvl][i+1:]
            items[0] = str(lvl + 1)
            yield ".".join(items)
        # try moving two items
        for i in range(len(items[lvl])):
            for j in range(i+1, len(items[lvl])):
                # TODO: check if can move items together
                items[lvl + 1] += items[lvl][i] + items[lvl][j]
                items[lvl] = items[lvl][:i] + items[lvl][i + 1:j] + items[lvl][j + 1:]
                items[0] = str(lvl + 1)
                yield ".".join(items)


# system state as a string
state = encode_string(floors)

seen_states = []
to_check = [(state, 0)]
last_moves = -1

while len(to_check):
    # get a new state
    state, moves = to_check.pop(0)
    # check if already visited
    if state in seen_states:
        continue
    else:
        seen_states.append(state)
    # show the progress
    if moves != last_moves:
        print(f"Checking move {moves}, {len(to_check)} paths to check, seen {len(seen_states)} different states")
        last_moves = moves
    # check if it's the solution
    if is_solution(state):
        print(f"Found the solution ({state}) in {moves} moves!")
        break
    # try moving stuff
    for new_state in try_move(state):
        print(new_state)
    break
