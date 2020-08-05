
# load the data
with open("Day06input.txt") as f:
    data = f.read().split("\n")


def decode(data):
    msg = []
    for i in range(len(data[0])):
        chars = {}
        for word in data:
            if word[i] in chars:
                chars[word[i]] += 1
            else:
                chars[word[i]] = 1
        msg.append([k for k, v in sorted(chars.items(), reverse=True, key=lambda item: item[1])][0])

    return "".join(msg)


print(decode(data))
