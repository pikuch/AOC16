from BunnyComp import BunnyComp

# load the data
with open("Day12input.txt") as f:
    data = f.read().split("\n")

comp = BunnyComp()
comp.load(data)
comp.run()

print(f"Value in register a: {comp.reg['a']}")

comp = BunnyComp()
comp.load(data)
comp.reg['c'] = 1
comp.run()

print(f"The correct value in register a: {comp.reg['a']}")
