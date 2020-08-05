
# position tracker
class Tracker:
    def __init__(self, x, y, d):
        self.x = x
        self.y = y
        self.d = d  # 0 = north
        self.visited = [(x, y)]
        self.revisited = []

    def distance_from_zero(self):
        return abs(self.x) + abs(self.y)

    def distance_from_zero_first_visited(self):
        return abs(self.revisited[0][0]) + abs(self.revisited[0][1])

    def check_revisited(self):
        if len(self.revisited) == 0:
            if (self.x, self.y) in self.visited:
                self.revisited.append((self.x, self.y))
            else:
                self.visited.append((self.x, self.y))

    def move(self, where):
        # change direction
        if where[0] == "L":
            self.d = (self.d + 3) % 4
        elif where[0] == "R":
            self.d = (self.d + 1) % 4
        else:
            pass  # shouldn't happen, we can go straight
        # walk
        steps = int(where[1:])
        if self.d == 0:
            for i in range(steps):
                self.y += 1
                self.check_revisited()
        elif self.d == 1:
            for i in range(steps):
                self.x += 1
                self.check_revisited()
        elif self.d == 2:
            for i in range(steps):
                self.y -= 1
                self.check_revisited()
        elif self.d == 3:
            for i in range(steps):
                self.x -= 1
                self.check_revisited()
        else:
            pass  # shouldn't happen, we stay where we are


# load the data
with open("Day01input.txt") as f:
    data = f.read()

# data cleanup
data = data.replace(' ', '')
data = data.split(',')

# decode the path
tracker = Tracker(0, 0, 0)
for item in data:
    tracker.move(item)

# print the answer
print(f"The target is at ({tracker.x}, {tracker.y}) which is {tracker.distance_from_zero()} blocks away.")
print(f"The first revisited position is at ({tracker.revisited[0][0]}, {tracker.revisited[0][1]})"
      f" which is {tracker.distance_from_zero_first_visited()} blocks away.")
