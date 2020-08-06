

class Node:
    def __init__(self, s):
        words = s.split()
        self.values = []
        self.connections = []
        self.passed_value = False
        if words[0] == "value":
            self.type = "input"
            self.values.append(int(words[1]))
            self.connections.append((words[4], words[5]))
        else:
            self.type = "bot"
            self.id = words[1]
            self.connections.append((words[5], words[6]))
            self.connections.append((words[10], words[11]))

    def __str__(self):
        s = "ID:" + self.type
        if self.type == "bot":
            s += self.id
        s += " \tValues:"
        for v in self.values:
            s += str(v) + " "
        s += " \tConnections:"
        for c in self.connections:
            s += c[0] + c[1] + " "
        return s


# load the data
with open("Day10input.txt") as f:
    data = f.read().split("\n")

nodes = []

for line in data:
    nodes.append(Node(line))

changes = True
while changes:
    changes = False
    # find a node to update
    for n in nodes:
        if not n.passed_value:
            if n.type == "input":
                for m in nodes:
                    if m.type == n.connections[0][0] and m.id == n.connections[0][1]:
                        m.values.append(n.values[0])
                        n.passed_value = True
                        changes = True
                        break
            else:
                if len(n.values) == 2:
                    for m in nodes:
                        if m.type == n.connections[0][0] and m.id == n.connections[0][1]:
                            m.values.append(min(n.values))
                            break
                    for m in nodes:
                        if m.type == n.connections[1][0] and m.id == n.connections[1][1]:
                            m.values.append(max(n.values))
                            n.passed_value = True
                            changes = True
                            break


for n in nodes:
    if 17 in n.values and 61 in n.values:
        print(str(n))

