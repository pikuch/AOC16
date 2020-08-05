
# load the data
with open("Day06input.txt") as f:
    data = f.read().split("\n")


def decode_high(data):
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


def decode_low(data):
    msg = []
    for i in range(len(data[0])):
        chars = {}
        for word in data:
            if word[i] in chars:
                chars[word[i]] += 1
            else:
                chars[word[i]] = 1
        msg.append([k for k, v in sorted(chars.items(), key=lambda item: item[1])][0])

    return "".join(msg)


print(f"The message from the most frequent characters is {decode_high(data)}")
print(f"The message from the least frequent characters is {decode_low(data)}")
