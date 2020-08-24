from BunnyComp import BunnyComp

# load the data
with open("Day25input.txt") as f:
    data = f.read().split("\n")

i = 0
while True:
    comp = BunnyComp()
    comp.load(data)
    comp.set_reg("a", i)
    result = comp.run()
    print(f"\r{i} {result}", end="")
    if result[:16] == [0, 1] * 8:
        print(f"\nFound it: {i} {result}")
        break
    i += 1
