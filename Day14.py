from hashlib import md5

# load the data
with open("Day14input.txt") as f:
    data = f.read()

# test
# data = "abc"


def run_search(stretch):
    candidates = []
    confirmed = []
    index = 0
    last_index = 10**10

    while index < last_index:

        s_in = data + str(index)
        s = md5(s_in.encode()).hexdigest()
        if stretch:
            for i in range(2016):
                s = md5(s.encode()).hexdigest()

        if index % 100 == 0:
            print(f"\rindex: {index:7d}, candidates: {len(candidates):5d}, found hashes: {len(confirmed):3d}", end="")

        for cand in candidates:
            if not cand[3]:
                if cand[2] + 1000 < index:
                    cand[3] = 1000
                    continue
                if s.find(cand[1] * 5) > -1:
                    confirmed.append(cand)
                    cand[3] = 1
                    if len(confirmed) == 64:
                        if last_index == 10**10:
                            last_index = index + 1000

        for i in range(len(s)-2):
            if s[i] == s[i+1] == s[i+2]:
                candidates.append([s, s[i], index, 0])
                break

        index += 1

    confirmed = sorted(confirmed, key=lambda x: x[2])

    return confirmed[63][2]


print(f"\nThe 64th hash found at index {run_search(stretch=False)}")
print(f"\nThe 64th stretched hash found at index {run_search(stretch=True)}")
