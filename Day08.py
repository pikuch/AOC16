

# screen class
class Screen:
    def __init__(self):
        self.width = 50
        self.height = 6
        self.pixels = []
        for h in range(self.height):
            new_row = [0] * self.width
            self.pixels.append(new_row)

    def show(self):
        for h in range(self.height):
            for w in range(self.width):
                if self.pixels[h][w]:
                    print("▓▓", end="")
                else:
                    print("░░", end="")
            print()

    def count_lit(self):
        counter = 0
        for h in range(self.height):
            for w in range(self.width):
                counter += self.pixels[h][w]
        return counter

    def run_cmd(self, cmd):
        words = cmd.split()
        if words[0] == "rect":
            dims = words[1].split("x")
            for w in range(int(dims[0])):
                for h in range(int(dims[1])):
                    self.pixels[h][w] = 1
        elif words[0] == "rotate":
            if words[1] == "row":
                place = int(words[2][2:])
                shift = int(words[4])
                new_row = []
                for i in range(self.width):
                    new_row.append((self.pixels[place][(i-shift+self.width) % self.width]))
                self.pixels[place] = new_row
            elif words[1] == "column":
                place = int(words[2][2:])
                shift = int(words[4])
                old_column = []
                for i in range(self.height):
                    old_column.append(self.pixels[i][place])
                for i in range(self.height):
                    self.pixels[i][place] = old_column[(i-shift+self.height) % self.height]
            else:
                print(f"Detected an error in instructions: {words[1]}")
        else:
            print(f"Detected an error in instructions: {words[0]}")


# load the data
with open("Day08input.txt") as f:
    data = f.read().split("\n")

screen = Screen()

for d in data:
    screen.run_cmd(d)

print(f"Number of lit pixels: {screen.count_lit()}")

screen.show()
