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

nodes = []
for item in data[2:]:
    nodes.append(Node(item))

viable_count = 0
for node1 in nodes:
    for node2 in nodes:
        if node1 != node2 and node1.used > 0 and node1.used <= node2.avail:
                viable_count += 1

print(f"Number of viable pairs: {viable_count}")

