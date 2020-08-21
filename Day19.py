
def remove_half(e, st):

    if len(e) % 2 == 0:
        next_start = st
    else:
        next_start = 1 - st

    new_e = []
    for i in range(len(e)):
        if i % 2 == st:
            new_e.append(e[i])

    return new_e, next_start


# load the data
with open("Day19input.txt") as f:
    data = int(f.read())

# test
# data = 5

elves = list(range(1, data + 1))

start = 0
while len(elves) > 1:
    elves, start = remove_half(elves, start)

print(elves[0])
