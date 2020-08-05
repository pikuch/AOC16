

# Keypad representation
class Keypad:
    def __init__(self):
        self.pad1 = [[0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 1, 2, 3, 0, 0],
                     [0, 0, 4, 5, 6, 0, 0],
                     [0, 0, 7, 8, 9, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]]
        self.pad2 = [[0, 0, 0, 0, 0, 0, 0],
                     [0, 0, 0, 1, 0, 0, 0],
                     [0, 0, 2, 3, 4, 0, 0],
                     [0, 5, 6, 7, 8, 9, 0],
                     [0, 0, "A", "B", "C", 0, 0],
                     [0, 0, 0, "D", 0, 0, 0],
                     [0, 0, 0, 0, 0, 0, 0]]
        self.x1, self.y1 = 3, 3
        self.x2, self.y2 = 1, 3
        self.code1 = ""
        self.code2 = ""
        self.delta_x = {"U":0, "D":0, "L":-1, "R":1, "\n":0}
        self.delta_y = {"U":-1, "D":1, "L":0, "R":0, "\n":0}

    def decode_moves(self, moves):
        for char in moves:
            self.x1 += self.delta_x[char]
            if self.pad1[self.y1][self.x1] == 0:
                self.x1 -= self.delta_x[char]
            self.y1 += self.delta_y[char]
            if self.pad1[self.y1][self.x1] == 0:
                self.y1 -= self.delta_y[char]
            self.x2 += self.delta_x[char]
            if self.pad2[self.y2][self.x2] == 0:
                self.x2 -= self.delta_x[char]
            self.y2 += self.delta_y[char]
            if self.pad2[self.y2][self.x2] == 0:
                self.y2 -= self.delta_y[char]
        self.code1 += str(self.pad1[self.y1][self.x1])
        self.code2 += str(self.pad2[self.y2][self.x2])


# load the data
with open("Day02input.txt") as f:
    data = f.readlines()

keypad = Keypad()

# decode the data
for line in data:
    keypad.decode_moves(line)

# print the code
print(f"The code could have been {keypad.code1} but is {keypad.code2}")
