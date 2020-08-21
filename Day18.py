
def calculate_rule(s):
    return "^" if s in traps else "."


def bordersafe_rule(s, i):
    if i == 0:
        return calculate_rule("." + s[i:i+2])
    elif i == len(s)-1:
        return calculate_rule(s[i-1:i+1] + ".")
    else:
        return calculate_rule(s[i-1:i+2])


def generate_row(tiles):
    new_row = ""
    for i in range(len(tiles[-1])):
        new_row += bordersafe_rule(tiles[-1], i)
    tiles.append(new_row)


def count_safe(tiles):
    safe = 0
    for row in tiles:
        safe += row.count(".")
    return safe


# load the data
with open("Day18input.txt") as f:
    data = f.read()

tiles = [data]
traps = ["^^.", ".^^", "^..", "..^"]

while len(tiles) < 40:
    generate_row(tiles)

print(f"There are {count_safe(tiles)} safe tiles in {len(tiles)} rows")

while len(tiles) < 400000:
    generate_row(tiles)

print(f"There are {count_safe(tiles)} safe tiles in {len(tiles)} rows")
