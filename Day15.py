
# load the data
with open("Day15input.txt") as f:
    data = f.read().split("\n")

# test
# data = ["Disc #1 has 5 positions; at time=0, it is at position 4.",
#         "Disc #2 has 2 positions; at time=0, it is at position 1."]


def interpret(data):
    ds = []
    index = 0
    for item in data:
        index += 1
        words = item.split()
        positions = int(words[3])
        current = (int(words[11][:-1]) + index) % positions
        ds.append([positions, current])
    return ds


def aligned(t):
    for d in discs:
        if (d[1] + t) % d[0]:
            return False
    return True


discs = interpret(data)

time = 0
while not aligned(time):
    time += 1

print(f"\rAlignment time: {time}")

time = 0
while not aligned(time):
    time += 1

print(f"\rAlignment time: {time}")
