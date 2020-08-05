

# figure out if the list of 3 numbers can represent a triangle
def can_be_triangle(t):
    ts = sorted(t)
    return ts[0] + ts[1] > ts[2]


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

# part 2

trisV = []

for i in range(len(tris)//3):
    for j in range(3):
        trisV.append([tris[i*3][j], tris[i*3+1][j], tris[i*3+2][j]])

print(f"The number of vertical triangles is {count_possible_triangles(trisV)}")
