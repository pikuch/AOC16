

# Keypad representation
class Keypad:
    def __init__(self):
        self.pad = [[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]]
        self.x, self.y = 1, 1
        self.digits = ""
        self.delta_x = {"U":0, "D":0, "L":-1, "R":1, "\n":0}
        self.delta_y = {"U":-1, "D":1, "L":0, "R":0, "\n":0}

    def decode_moves(self, moves):
        for char in moves:
            self.x += self.delta_x[char]
            if self.x < 0:
                self.x = 0
            if self.x > 2:
                self.x = 2
            self.y += self.delta_y[char]
            if self.y < 0:
                self.y = 0
            if self.y > 2:
                self.y = 2
        self.digits += str(self.pad[self.y][self.x])


# load the data
with open("Day02input.txt") as f:
    data = f.readlines()

keypad = Keypad()

# decode the data
for line in data:
    keypad.decode_moves(line)

# print the code
print(f"The code is {keypad.digits}")
