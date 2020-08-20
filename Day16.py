
# load the data
with open("Day16input.txt") as f:
    data = f.read()

length = 272

# test
# data = "10000"
# length = 20


def fill_disc(d, length):
    while len(d) < length:
        d = d + "0" + d[::-1].replace("0", "o").replace("1", "0").replace("o", "1")
    return d[:length]


def get_checksum(d):
    while len(d) % 2 == 0:
        print(f"shortening {len(d)}...")
        new_d = ""
        for i in range(len(d)//2):
            if d[2*i] == d[2*i+1]:
                new_d += "1"
            else:
                new_d += "0"
        d = new_d
    return d


filled = fill_disc(data, length)
print(f"Checksum is: {get_checksum(filled)}")

length = 35651584
filled = fill_disc(data, length)
print(f"Checksum is: {get_checksum(filled)}")
