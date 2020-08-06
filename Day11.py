import numpy as np
from itertools import permutations

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
