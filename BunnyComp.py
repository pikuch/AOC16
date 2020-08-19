class BunnyComp:
    def __init__(self):
        self.reg = {
            "a": 0,
            "b": 0,
            "c": 0,
            "d": 0
        }
        self.program = []
        self.pc = 0
        self.ops = {
            "cpy": self.cpy,
            "inc": self.inc,
            "dec": self.dec,
            "jnz": self.jnz
        }

    #####################################################
    # OPERATIONS

    def cpy(self, args):
        if args[0] in self.reg:
            self.reg[args[1]] = self.reg[args[0]]
        else:
            self.reg[args[1]] = int(args[0])
        self.pc += 1

    def inc(self, args):
        self.reg[args[0]] += 1
        self.pc += 1

    def dec(self, args):
        self.reg[args[0]] -= 1
        self.pc += 1

    def jnz(self, args):
        if args[0] in self.reg:
            if self.reg[args[0]]:
                self.pc += int(args[1])
            else:
                self.pc += 1
        else:
            if int(args[0]):
                self.pc += int(args[1])
            else:
                self.pc += 1

    #####################################################

    def load(self, instructions):
        for inst in instructions:
            self.program.append(inst.split())
        self.pc = 0

    def run(self):
        while True:
            if 0 <= self.pc < len(self.program):
                self.exec(self.program[self.pc])
            else:
                break

    def exec(self, inst):
        if inst[0] in self.ops:
            self.ops[inst[0]](inst[1:])
