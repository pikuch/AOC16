from BunnyComp import BunnyComp

# load the data
with open("Day23input.txt") as f:
    data = f.read().split("\n")

# test
# data = ["cpy 2 a", "tgl a", "tgl a", "tgl a", "cpy 1 a", "dec a", "dec a"]

bc = BunnyComp()
bc.load(data)
bc.reg[0] = 12
bc.run()
print(bc.reg[0])
