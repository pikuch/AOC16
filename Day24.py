import numpy as np
from itertools import permutations


class Labyrinth:
    def __init__(self, x, y):
        self.m = np.zeros((y, x), dtype=np.int32)
        self.poi = {}
        self.max_point = 0
        self.distances = {}

    def display(self):
        for y in range(self.m.shape[0]):
            for x in range(self.m.shape[1]):
                if (x, y) in self.poi:
                    print(self.poi[(x, y)], end="")
                elif self.m[y, x] == 1:
                    print("#", end="")
                else:
                    print(" ", end="")
            print("")

    def add_wall(self, x, y):
        self.m[y, x] = 1

    def add_poi(self, x, y, n):
        self.poi[(x, y)] = n
        self.poi[n] = (x, y)
        if n > self.max_point:
            self.max_point = n

    def a_star(self, p1, p2):
        x, y = self.poi[p1]
        target_x, target_y = self.poi[p2]
        distmap = np.full_like(self.m, -1)
        distmap[y, x] = 0
        to_check = [(x, y, 0)]
        while True:  # assuming there is always a path (!)
            x, y, moves = to_check.pop(0)
            if x == target_x and y == target_y:
                return moves
            if self.m[y - 1, x] == 0:
                if distmap[y - 1, x] == -1:
                    distmap[y - 1, x] = moves + 1
                    to_check.append((x, y - 1, moves + 1))
            if self.m[y + 1, x] == 0:
                if distmap[y + 1, x] == -1:
                    distmap[y + 1, x] = moves + 1
                    to_check.append((x, y + 1, moves + 1))
            if self.m[y, x - 1] == 0:
                if distmap[y, x - 1] == -1:
                    distmap[y, x - 1] = moves + 1
                    to_check.append((x - 1, y, moves + 1))
            if self.m[y, x + 1] == 0:
                if distmap[y, x + 1] == -1:
                    distmap[y, x + 1] = moves + 1
                    to_check.append((x + 1, y, moves + 1))

    def dist_between(self, p1, p2):
        if (p1, p2) in self.distances:
            return self.distances[(p1, p2)]
        # else calculate distance
        dist = self.a_star(p1, p2)
        self.distances[(p1, p2)] = dist
        self.distances[(p2, p1)] = dist
        return dist

    def sum_path(self, points):
        dist = 0
        for i in range(len(points) - 1):
            dist += self.dist_between(points[i], points[i + 1])
        return dist


# load the data
with open("Day24input.txt") as f:
    data = f.read().split("\n")

vents = Labyrinth(len(data[0]), len(data))
for row in range(len(data)):
    for col in range(len(data[0])):
        if data[row][col] == "#":
            vents.add_wall(col, row)
        elif data[row][col] == ".":
            pass
        else:
            vents.add_poi(col, row, int(data[row][col]))

shortest_dist = 10**10
shortest_return = 10**10
for perm in permutations(range(1, vents.max_point + 1)):
    new_dist = vents.sum_path([0] + list(perm))
    if new_dist < shortest_dist:
        shortest_dist = new_dist
    new_return = vents.sum_path([0] + list(perm) + [0])
    if new_return < shortest_return:
        shortest_return = new_return

print(shortest_dist, shortest_return)
