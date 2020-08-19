from BunnyComp import BunnyComp

# load the data
with open("Day12input.txt") as f:
    data = f.read().split("\n")

comp = BunnyComp()
comp.load(data)
comp.run()

print(f"Result 1 found: {comp.get_reg('a')}")

comp = BunnyComp()
comp.load(data)
comp.set_reg('c', 1)
comp.run()

print(f"Result 2 found: {comp.get_reg('a')}")
