from functools import reduce


def cutout(what, wlist):
    low, high = map(int, what.split("-"))
    new_wlist = []
    for item in wlist:
        if low <= item[0] <= high < item[1]:
            new_wlist.append([high + 1, item[1]])
        elif item[0] < low <= item[1] <= high:
            new_wlist.append([item[0], low - 1])
        elif low > item[0] and high < item[1]:
            new_wlist.append([item[0], low - 1])
            new_wlist.append([high + 1, item[1]])
        elif low <= item[0] and high >= item[1]:
            pass
        else:
            new_wlist.append(item)

    return new_wlist


# load the data
with open("Day20input.txt") as f:
    data = f.read().split("\n")

whitelist = [[0, 2**32-1]]

# test
# whitelist = [[0, 9]]
# data = ["5-8", "0-2", "4-7"]

for d in data:
    whitelist = cutout(d, whitelist)

print(f"The lowest not blocked IP is {sorted(whitelist, key=lambda x: x[0])[0][0]}")

print(f"The number of allowed IPs is {reduce(lambda x, y: x + y[1] - y[0] + 1, whitelist, 0)}")
