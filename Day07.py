

# transmission class
class Trans:
    def __init__(self, tstr):
        self.msg = tstr
        self.regular = []
        self.hypernet = []
        self.parse_msg()
    
    def parse_msg(self):
        s = self.msg
        while len(s):
            opening = s.find("[")
            closing = s.find("]")
            if opening < 0 and closing < 0:
                self.regular.append(s[:])
                s = ""
            elif opening < 0:
                self.hypernet.append(s[0:closing])
                s = s[closing+1:]
            elif closing < 0:
                print("Error: no closing bracket found")
                exit(-1)
            else:
                if opening < closing:
                    self.regular.append(s[0:opening])
                    s = s[opening+1:]
                else:
                    self.hypernet.append(s[0:closing])
                    s = s[closing+1:]

    def contains_ABBA(self, s):
        for i in range(max(len(s)-3, 0)):
            if s[i] == s[i+3] and s[i+1] == s[i+2] and s[i] != s[i+1]:
                return True
        return False

    def supports_TLS(self):
        abba_in_regular = False
        for r in self.regular:
            if self.contains_ABBA(r):
                abba_in_regular = True
                break
        abba_in_hypernet = False
        for h in self.hypernet:
            if self.contains_ABBA(h):
                abba_in_hypernet = True
                break

        return abba_in_regular and not abba_in_hypernet


# load the data
with open("Day07input.txt") as f:
    data = f.read().split("\n")

msgs = []

for d in data:
    msgs.append(Trans(d))

support_count = 0

for m in msgs:
    if m.supports_TLS():
        support_count += 1

print(f"Number of IPs supporting TLS = {support_count}")
