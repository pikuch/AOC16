
def calculate_rule(s):
    return "^" if s in traps else "."


def bordersafe_rule(s, i):
    if i == 0:
        return calculate_rule("." + s[i:i+2])
    elif i == len(s)-1:
        return calculate_rule(s[i-1:i+1] + ".")
    else:
        return calculate_rule(s[i-1:i+2])


def count_safe(tiles):
    return tiles.count(".")


def generate_and_count(tiles, rows):
    empties = count_safe(tiles)
    for row in range(rows-1):
        if row % 10000 == 0:
            print(f"\rCalculating row {row} / {rows}", end="")
        new_row = ""
        for i in range(len(tiles)):
            new_row += bordersafe_rule(tiles, i)
        tiles = new_row
        empties += count_safe(tiles)
    return empties


# load the data
with open("Day18input.txt") as f:
    tiles = f.read()

traps = ["^^.", ".^^", "^..", "..^"]

empties = generate_and_count(tiles, 40)
print(f"\nThere are {empties} safe tiles in 40 rows")

empties = generate_and_count(tiles, 400000)
print(f"\nThere are {empties} safe tiles in 400000 rows")
