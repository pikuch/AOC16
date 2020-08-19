from hashlib import md5
from binascii import hexlify

# load the data
with open("Day14input.txt") as f:
    data = f.read()

# test
data = "abc"

candidates = []
confirmed = []
index = 0
last_index = None

while True:
    hash_in = data + str(index)
    hash_out = hexlify(md5(bytes(hash_in, "ascii")).digest())
    s = str(hash_out, "utf-8")

    if index % 1000 == 0:
        print(f"\rindex: {index:7d}, candidates: {len(candidates):5d}, found hashes: {len(confirmed):3d}", end="")

    for cand in candidates:
        if cand[2] + 1000 < index:
            candidates.remove(cand)

    for h, char, i in candidates:
        if s.find(char * 5) > -1:
            confirmed.append((h, char, i))
            if len(confirmed) == 64:
                if last_index is None:
                    last_index = index + 1000

    for i in range(len(s)-2):
        if s[i] == s[i+1] == s[i+2]:
            candidates.append((s, s[i], index))
            break

    index += 1
    if index == last_index:
        break

confirmed = sorted(confirmed, key=lambda x: x[2])

print(f"\nThe last hash found at index {confirmed[63][2]}")

# part 2

candidates = []
confirmed = []
index = 0
last_index = None

while True:
    hash_in = data + str(index)
    hash_out = hexlify(md5(bytes(hash_in, "ascii")).digest())
    s = str(hash_out, "utf-8")

    if index % 1000 == 0:
        print(f"\rindex: {index:7d}, candidates: {len(candidates):5d}, found hashes: {len(confirmed):3d}", end="")

    for cand in candidates:
        if cand[2] + 1000 < index:
            candidates.remove(cand)

    for h, char, i in candidates:
        if s.find(char * 5) > -1:
            confirmed.append((h, char, i))
            if len(confirmed) == 64:
                if last_index is None:
                    last_index = index + 1000

    for i in range(len(s)-2):
        if s[i] == s[i+1] == s[i+2]:
            candidates.append((s, s[i], index))
            break

    index += 1
    if index == last_index:
        break

confirmed = sorted(confirmed, key=lambda x: x[2])

for i, conf in enumerate(confirmed):
    print(f"{i}: {conf}")

print(f"\nThe last hash found at index {confirmed[63][2]}")
