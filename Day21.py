
class Scrambler:
    def __init__(self, s):
        self.s = list(s)

    def scramble(self, ops):
        for operation in ops:
            self.decode_apply(operation)

    def get(self):
        return "".join(self.s)

    def decode_apply(self, op):
        words = op.split()
        if words[0] == "swap":
            if words[1] == "position":
                self.swap_position(int(words[2]), int(words[5]))
            elif words[1] == "letter":
                self.swap_letter(words[2], words[5])
            else:
                print(f"[ERROR] Illegal operation: {words}")
                exit(1)
        elif words[0] == "reverse":
            self.reverse(int(words[2]), int(words[4]))
        elif words[0] == "rotate":
            if words[1] == "right":
                self.rotate_right(int(words[2]))
            elif words[1] == "left":
                self.rotate_left(int(words[2]))
            elif words[1] == "based":
                self.rotate_based(words[6])
            else:
                print(f"[ERROR] Illegal operation: {words}")
                exit(1)
        elif words[0] == "move":
            self.move(int(words[2]), int(words[5]))
        else:
            print(f"[ERROR] Illegal operation: {words}")
            exit(1)

    def swap_position(self, a, b):
        self.s[a], self.s[b] = self.s[b], self.s[a]

    def swap_letter(self, a, b):
        ns = []
        for item in self.s:
            if item == a:
                ns.append(b)
            elif item == b:
                ns.append(a)
            else:
                ns.append(item)
        self.s = ns

    def reverse(self, a, b):
        self.s = self.s[:a] + self.s[a:b+1][::-1] + self.s[b+1:]

    def rotate_left(self, a):
        for i in range(a):
            self.s = self.s[1:] + [self.s[0]]

    def rotate_right(self, a):
        for i in range(a):
            self.s = [self.s[-1]] + self.s[0:-1]

    def rotate_based(self, a):
        index = self.get().find(a)
        index += 2 if index >= 4 else 1
        self.rotate_right(index)

    def move(self, a, b):
        self.s.insert(b, self.s.pop(a))


# load the data
with open("Day21input.txt") as f:
    data = f.read().split("\n")
word = "abcdefgh"

# test
# data = ["swap position 4 with position 0",
#         "swap letter d with letter b",
#         "reverse positions 0 through 4",
#         "rotate left 1 step",
#         "move position 1 to position 4",
#         "move position 3 to position 0",
#         "rotate based on position of letter b",
#         "rotate based on position of letter d"]
# word = "abcde"

password = Scrambler(word)
password.scramble(data)

print(f"The scrambled password is {password.get()}")
