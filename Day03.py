

# figure out if the list of 3 numbers can represent a triangle
def can_be_triangle(t):
    t.sort()
    return t[0] + t[1] > t[2]


# count cases which can be triangles
def count_possible_triangles(tris):
    count = 0
    for t in tris:
        if can_be_triangle(t):
            count += 1
    return count


# load the data
with open("Day03input.txt") as f:
    data = f.readlines()

tris = []

# convert data to numbers
for line in data:
    tri = []
    for num in line.split():
        tri.append(int(num))
    tris.append(tri)

print(f"The number of possible triangles is {count_possible_triangles(tris)}")
