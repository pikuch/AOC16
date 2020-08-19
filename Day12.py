from BunnyComp import BunnyComp
from time import time_ns

# load the data
with open("Day12input.txt") as f:
    data = f.read().split("\n")

comp = BunnyComp()
comp.load(data)
t0 = time_ns()
comp.run()
td = time_ns() - t0

print(f"Time taken: {td//(10**6):_d} ms")
print(f"Result 1 found: {comp.reg['a']}")

comp = BunnyComp()
comp.load(data)
comp.reg['c'] = 1
t0 = time_ns()
comp.run()
td = time_ns() - t0

print(f"Time taken: {td//(10**6):_d} ms")
print(f"Result 2 found: {comp.reg['a']}")
