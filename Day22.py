class Node:
    def __init__(self, row):
        words = row.split()
        address = words[0].split("-")
        self.x = int(address[1][1:])
        self.y = int(address[2][1:])
        self.size = int(words[1][:-1])
        self.used = int(words[2][:-1])
        self.avail = int(words[3][:-1])

    def to_dict(self):
        return {"x": self.x, "y": self.y, "size": self.size, "used": self.used, "available": self.avail}


# load the data
with open("Day22input.txt") as f:
    data = f.read().split("\n")

nodes = {}
for item in data[2:]:
    n = Node(item)
    nodes[(n.x, n.y)] = n

viable_count = 0
for node1 in nodes.values():
    for node2 in nodes.values():
        if node1 != node2 and node1.used > 0 and node1.used <= node2.avail:
                viable_count += 1

print(f"Number of viable pairs: {viable_count}")

# part 2

# find the dimensions of the grid
max_x, max_y = 0, 0
for node in nodes.keys():
    if node[0] > max_x:
        max_x = node[0]
    if node[1] > max_y:
        max_y = node[1]

# show the grid
for y in range(max_y + 1):
    for x in range(max_x + 1):
        if nodes[(x, y)].used > 100:
            print(" X ", end="")
        elif nodes[(x, y)].used == 0:
            print("   ", end="")
        else:
            print(" . ", end="")
    print("")

print("35 + 5 * 33 = 200 (calculated by hand)")
