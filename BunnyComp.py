class BunnyComp:
    def __init__(self):
        self.reg = [0] * 4
        self.program = []
        self.pc = 0
        self.ops = {
            "cpy": self.cpy,
            "inc": self.inc,
            "dec": self.dec,
            "jnz": self.jnz,
            "tgl": self.tgl
        }

    #####################################################
    # OPERATIONS

    def cpy(self, args):
        if args[1] < 4:  # skip if constant
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

    def tgl(self, args):
        if self.pc + self.reg[args[0]] < 0 or self.pc + self.reg[args[0]] >= len(self.program):
            self.pc += 1
            return
        mod = self.program[self.pc + self.reg[args[0]]]
        if mod[0] == "inc":
            mod[0] = "dec"
        elif mod[0] == "dec":
            mod[0] = "inc"
        elif mod[0] == "tgl":
            mod[0] = "inc"
        elif mod[0] == "jnz":
            mod[0] = "cpy"
        elif mod[0] == "cpy":
            mod[0] = "jnz"
        else:
            print(f"Illegal instruction: {mod}")
            exit(1)
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
            # try:
            #     if inst[0] == "inc":
            #         inst1 = self.program[self.pc + 1]
            #         inst2 = self.program[self.pc + 2]
            #         if inst1[0] == "dec" and inst2[0] == "jnz":
            #             if inst1[1] == inst2[1] and self.reg[inst2[2]] == -2:
            #                 self.reg[inst[1]] += self.reg[inst1[1]]
            #                 self.reg[inst1[1]] = 0
            #                 self.pc += 3
            #                 inst = self.program[self.pc]
            # except IndexError:
            #     pass

            # multiplication loop speedup
            # ["cpy 25 b", "inc a", "dec b", "jnz b -2", "dec c", "jnz c -5"]
            try:
                if inst[0] == "cpy":
                    ninst = self.program[self.pc:self.pc+6]
                    if ninst[1][0] == "inc" and ninst[2][0] == ninst[4][0]== "dec" and ninst[3][0] == ninst[5][0] == "jnz":
                        if ninst[0][2] == ninst[2][1] == ninst[3][1] and ninst[4][1] == ninst[5][1] and self.reg[ninst[3][2]] == -2 and self.reg[ninst[5][2]] == -5:
                            self.reg[ninst[1][1]] += self.reg[ninst[0][1]] * self.reg[ninst[4][1]]
                            self.reg[ninst[2][1]] = 0
                            self.reg[ninst[4][1]] = 0
                            self.pc += 6
                            inst = self.program[self.pc]
            except IndexError:
                pass
            self.ops[inst[0]](inst[1:])
