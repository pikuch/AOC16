# load the data
with open("Day01input.txt") as f:
    data = f.read()

# data cleanup
data = data.replace(' ', '')
data = data.split(',')


# find a new position
def decode_item(instruction, d, x, y):
    get_L = {"N": "W", "W": "S", "S": "E", "E": "N"}
    get_R = {"W": "N", "N": "E", "E": "S", "S": "W"}
    steps = {"N": [0, 1], "W": [-1, 0], "S": [0, -1], "E": [1, 0]}

    if instruction[0] == "L":
        d = get_L[d]
    elif instruction[0] == "R":
        d = get_R[d]
    else:
        print(f"Illegal instruction encountered: {instruction}")
        exit(-1)

    x += int(instruction[1:]) * steps[d][0]
    y += int(instruction[1:]) * steps[d][1]

    return d, x, y


# decode the path
direction = "N"
x, y = 0, 0

for item in data:
    direction, x, y = decode_item(item, direction, x, y)

# print the answer
print(f"The target is at ({x}, {y}) which is {abs(x)+abs(y)} blocks away.")
