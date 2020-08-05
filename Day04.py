

# room representation
class Room:
    def __init__(self, s):
        self.name = s[0:-11]
        self.sector = int(s[-11:-8])
        self.checksum = s[-7:-2]
        self.is_legit = self.verify()
        self.real_name = ""
        self.get_real_name()

    def verify(self):
        n = self.name.replace("-", "")
        reps = {}
        for char in n:
            if char in reps:
                reps[char] += 1
            else:
                reps[char] = 1
        ordered_chars = [k for k, v in sorted(reps.items(), key=lambda item: (-item[1], item[0]))]

        return self.checksum == "".join(ordered_chars[:5])

    def get_real_name(self):
        if self.is_legit:
            for char in self.name:
                if char == "-":
                    self.real_name += " "
                else:
                    self.real_name += chr(ord("a") + ((ord(char) - ord("a")) + self.sector) % (ord("z") - ord("a") + 1))
        else:
            self.real_name = "checksum_failed"


# load the data
with open("Day04input.txt") as f:
    data = f.readlines()

rooms = []

# prepare the data
for line in data:
    rooms.append(Room(line))

# count real rooms' sector IDs
sector_sum = 0

for r in rooms:
    if r.is_legit:
        sector_sum += r.sector

print(f"The sum of sector IDs of real rooms is {sector_sum}")

for r in rooms:
    if r.real_name.find("north") >= 0:
        print(f"Found room {r.real_name} in sector {r.sector}")
