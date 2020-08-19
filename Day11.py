from copy import deepcopy
from itertools import permutations

# load the data
with open("Day11input.txt") as f:
    data = f.read().split("\n")

# testing data
# data = ["hyd M, lit M", "hyd G", "lit G", ""]

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


def encode_array(floors):
    s = []
    for i in range(len(elements)):
        s.append([0, 0])

    for floor_number, floor in enumerate(floors):
        if len(floor):
            for el in floor:
                if el[1] == "G":
                    s[elements.index(el[0])][0] = floor_number
                else:
                    s[elements.index(el[0])][1] = floor_number

    return [0, s]


def is_solution(state):
    for pair in state[1]:
        if pair[0] != 3 or pair[1] != 3:
            return False
    return True


def get_hash(state):
    s = str(state[0])
    for pair in state[1]:
        s += str(pair[0]) + str(pair[1])
    return s


def get_new_hashes(state):
    hashes = set()
    for perm in permutations(state[1]):
        hashes.add(get_hash([state[0], perm]))
    return hashes


def good_state(state):
    global seen_states
    # find radiation zones
    radiation = [0] * 4
    for pair in state[1]:
        radiation[pair[0]] = 1
    # find unprotected chips
    for pair in state[1]:
        if radiation[pair[1]] and pair[0] != pair[1]:
            return False
    # check if the state (or its equivalent) has already been visited
    if get_hash(state) in seen_states:
        return False
    # add new states to seen states
    seen_states |= get_new_hashes(state)
    return True


def possible_moves(state):
    move_list = []

    lowest_nonempty_floor = 3
    for pair in state[1]:
        if pair[0] < lowest_nonempty_floor:
            lowest_nonempty_floor = pair[0]
        if pair[1] < lowest_nonempty_floor:
            lowest_nonempty_floor = pair[1]

    if state[0] < 3:  # we can go up
        # try moving two elements up
        for pair1 in range(len(state[1])):
            for pair2 in range(pair1, len(state[1])):
                for i1 in range(2):
                    for i2 in range(2):
                        if state[1][pair1][i1] == state[0] and state[1][pair2][i2] == state[0]:
                            if pair1 == pair2 and i1 == i2:
                                continue
                            new_state = deepcopy(state)
                            new_state[0] += 1
                            new_state[1][pair1][i1] += 1
                            new_state[1][pair2][i2] += 1
                            if good_state(new_state):
                                move_list.append(new_state)

        # try moving one element up
        for pair in range(len(state[1])):
            for i in range(2):
                if state[1][pair][i] == state[0]:
                    new_state = deepcopy(state)
                    new_state[0] += 1
                    new_state[1][pair][i] += 1
                    if good_state(new_state):
                        move_list.append(new_state)

    if state[0] > lowest_nonempty_floor:  # we can go down
        # try moving one element down
        for pair in range(len(state[1])):
            for i in range(2):
                if state[1][pair][i] == state[0]:
                    new_state = deepcopy(state)
                    new_state[0] -= 1
                    new_state[1][pair][i] -= 1
                    if good_state(new_state):
                        move_list.append(new_state)
    return move_list


def can_move_with(el0, ty0, el1, ty1):
    if ty0 == ty1:
        return True
    else:
        if el0 == el1:
            return True
    return False


def can_move(s, lvl, el, ty):
    if ty == 0:  # a new generator
        for check in range(len(elements)):
            if check != el:
                if s[lvl][check][1] and not s[lvl][check][0]:
                    return False
    else:  # a new microchip
        if not s[lvl][el][0]:
            for check in range(len(elements)):
                if s[lvl][check][0]:
                    return False
    return True


def something_broke(s, lvl):
    for el in range(len(elements)):
        if s[lvl][el][1] and not s[lvl][el][0]:
            for check in range(len(elements)):
                if s[lvl][check][0]:
                    return True


def not_seen(ns, lvl, seen):
    for i in range(len(seen)):
        if np.array_equiv(ns, seen[i][0]) and lvl == seen[i][1]:
            return False
    return True


# system state as an array
state = np.zeros((4, len(elements), 2), dtype=np.uint8)

for floor_number, floor in enumerate(floors):
    if not len(floor):
        continue
    for el in floor:
        state[floor_number][elements.index(el[0])][0 if el[1] == "G" else 1] = 1

to_try = [(state, 0, 0)]
seen = [(state, 0)]
last_moves = -1

while len(to_try):
    state, elevator, moves = to_try.pop(0)
    if moves != last_moves:
        print(f"Moves: {moves}, to check: {len(to_try)}")
    last_moves = moves
    if something_broke(state, elevator):  # we got into an illegal state
        continue
    if elevator == 3:
        if state[3].sum() == 2 * len(elements):
            print(f"Everything is on the 4th floor in {moves} moves")
            break
    # try moving single items
    for item_type in range(2):
        for element in range(len(elements)):
            if state[elevator][element][item_type]:
                if elevator - 1 >= 0 and can_move(state, elevator, element, item_type):
                    ns = np.copy(state)
                    ns[elevator][element][item_type] = 0
                    ns[elevator - 1][element][item_type] = 1
                    if not_seen(ns, elevator, seen):
                        seen.append((ns, elevator))
                        to_try.append((ns, elevator - 1, moves + 1))
                if elevator + 1 < 4 and can_move(state, elevator, element, item_type):
                    ns = np.copy(state)
                    ns[elevator][element][item_type] = 0
                    ns[elevator + 1][element][item_type] = 1
                    if not_seen(ns, elevator, seen):
                        seen.append((ns, elevator))
                        to_try.append((ns, elevator + 1, moves + 1))
    # try moving pairs of items
    for item_types in permutations(range(2), 2):
        for elements in permutations(range(len(elements)), 2):
            if state[elevator][elements[0]][item_types[0]] and state[elevator][elements[1]][item_types[1]]:
                if can_move_with(elements[0], item_types[0], elements[1], item_types[1]):
                    if elevator - 1 >= 0:
                        ns = np.copy(state)
                        ns[elevator][elements[0]][item_types[0]] = 0
                        ns[elevator - 1][elements[0]][item_types[0]] = 1
                        ns[elevator][elements[1]][item_types[1]] = 0
                        ns[elevator - 1][elements[1]][item_types[1]] = 1
                        if not_seen(ns, elevator, seen):
                            seen.append((ns, elevator))
                            to_try.append((ns, elevator - 1, moves + 1))
                    if elevator + 1 < 4:
                        ns = np.copy(state)
                        ns[elevator][elements[0]][item_types[0]] = 0
                        ns[elevator + 1][elements[0]][item_types[0]] = 1
                        ns[elevator][elements[1]][item_types[1]] = 0
                        ns[elevator + 1][elements[1]][item_types[1]] = 1
                        if not_seen(ns, elevator, seen):
                            seen.append((ns, elevator))
                            to_try.append((ns, elevator + 1, moves + 1))


########################################################################
# part 2
# takes a few minutes, but it works

# system state as an array
state = encode_array(floors)
state[1].extend([[0, 0], [0, 0]])

seen_states = {get_hash(state)}
to_check = [(state, 0)]
last_moves = -1

while len(to_check):
    # get a new state
    state, moves = to_check.pop(0)
    # show the progress
    if moves != last_moves:
        print(f"\rChecking move {moves:2d}, {len(to_check):6d} paths to check, {len(seen_states):6d} states seen", end="")
        last_moves = moves
    # check if it's the solution
    if is_solution(state):
        print(f"\nFound the solution to part 2 in {moves} moves!")
        break
    # try moving stuff
    for new_state in possible_moves(state):
        to_check.append((new_state, moves + 1))
