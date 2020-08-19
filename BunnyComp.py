class BunnyComp:
    def __init__(self):
        self.reg = [0] * 4
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
        self.reg[args[1]] = self.reg[args[0]]
        self.pc += 1

    def inc(self, args):
        self.reg[args[0]] += 1
        self.pc += 1

    def dec(self, args):
        self.reg[args[0]] -= 1
        self.pc += 1

    def jnz(self, args):
        if self.reg[args[0]]:
            self.pc += self.reg[args[1]]
        else:
            self.pc += 1

    #####################################################

    def get_reg(self, name):
        return self.reg[ord(name) - ord('a')]

    def set_reg(self, name, value):
        self.reg[ord(name) - ord('a')] = value

    def load(self, instructions):
        reg_names = "abcd"
        for inst in instructions:
            ilist = inst.split()
            for i in range(1, len(ilist)):
                if ilist[i] in reg_names:
                    ilist[i] = ord(ilist[i]) - ord('a')
                else:
                    self.reg.append(int(ilist[i]))
                    ilist[i] = len(self.reg) - 1

            self.program.append(ilist)
        self.pc = 0

    def run(self):
        while True:
            try:
                inst = self.program[self.pc]
            except IndexError:
                break
            # tight loop speedup
            try:
                if inst[0] == "inc":
                    inst1 = self.program[self.pc + 1]
                    inst2 = self.program[self.pc + 2]
                    if inst1[0] == "dec" and inst2[0] == "jnz":
                        if inst1[1] == inst2[1] and self.reg[inst2[2]] == -2:
                            self.reg[inst[1]] += self.reg[inst1[1]]
                            self.reg[inst1[1]] = 0
                            self.pc += 3
                            inst = self.program[self.pc]
            except IndexError:
                pass
            self.ops[inst[0]](inst[1:])
