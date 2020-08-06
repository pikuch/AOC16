

# decode a repetition marker
def decode(marker):
    nums = marker.split("x")
    return int(nums[0]), int(nums[1])


# decompress a given string
def decompress(s):
    result = ""
    pos = 0
    while pos < len(s):
        if s[pos] != "(":
            result += s[pos]
            pos += 1
        else:
            closing_pos = s[pos:].find(")")
            marker = s[pos+1:pos+closing_pos]
            nchars, reps = decode(marker)
            pos = pos + closing_pos + 1
            result += s[pos:pos+nchars] * reps
            pos += nchars
    return result


# load the data
with open("Day09input.txt") as f:
    data = f.read()

print(f"The decompressed length is {len(decompress(data))}")
