# load the data
with open("Day01input.txt") as f:
    data = f.read()

# data cleanup
data = data.replace(' ', '')
data = data.split(',')


# position tracker
class Tracker:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d # 0 = north
    def distance_to_zero(self):
        return abs(self.x) + abs(self.y)
    def move(self, where):


# find a new position
def decode_item(instruction, d, x, y, visited):
    get_L = {"N": "W", "W": "S", "S": "E", "E": "N"}
    get_R = {"W": "N", "N": "E", "E": "S", "S": "W"}
    what_steps = {"N": [0, 1], "W": [-1, 0], "S": [0, -1], "E": [1, 0]}

    if instruction[0] == "L":
        d = get_L[d]
    elif instruction[0] == "R":
        d = get_R[d]
    else:
        print(f"Illegal instruction encountered: {instruction}")
        exit(-1)

    steps = int(instruction[1:])

    for s in range

    x += steps * what_steps[d][0]
    y += steps * what_steps[d][1]

    return d, x, y


# decode the path

for item in data:
    direction, x, y = decode_item(item, direction, x, y, visited)

# print the answer
print(f"The target is at ({x}, {y}) which is {abs(x)+abs(y)} blocks away.")
