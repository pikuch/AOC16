
class Node:
    def __init__(self, val):
        self.val = val
        self.next = self
        self.prev = self

    def append(self, val):
        new_node = Node(val)
        new_node.prev = self
        new_node.next = self.next
        self.next.prev = new_node
        self.next = new_node
        return new_node

    def remove(self):
        next_node = self.next
        prev_node = self.prev
        next_node.prev = prev_node
        prev_node.next = next_node
        return next_node

    def print_ring(self):
        first = self
        current = self
        s = ""
        while True:
            s += "(" + str(current.val) + ")"
            if current == current.next.prev:
                s += "="
            current = current.next
            if current == first:
                break
        print(s)


def remove_opposite(data):
    # make a list
    first = current = Node(1)
    for i in range(2, data + 1):
        current = current.append(i)
        if i == data//2 + 1:
            opposite = current

    length = data
    current = first

    while length > 1:
        # if length % 1000 == 0:
        #     print(f"\r{length} elves left", end="")
        opposite = opposite.remove()
        if length % 2 == 1:
            opposite = opposite.next
        current = current.next
        length -= 1

    return current.val


def remove_every_next(e):
    st = 0
    while len(e) > 1:
        if len(e) % 2 == 0:
            next_start = st
        else:
            next_start = 1 - st

        new_e = []
        for i in range(len(e)):
            if i % 2 == st:
                new_e.append(e[i])
        st = next_start
        e = new_e
    return e[0]


# load the data
with open("Day19input.txt") as f:
    data = int(f.read())

# test
# data = 5

elves = list(range(1, data + 1))
elf = remove_every_next(elves)
print(f"\nelf {elf} wins")

elf = remove_opposite(data)
print(f"\nnow elf {elf} wins")
