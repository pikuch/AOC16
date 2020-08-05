from hashlib import md5
from binascii import hexlify

# load the data
with open("Day05input.txt") as f:
    door = f.read()


def get_password(door):
    passwd = ["."] * 8
    next_pos = 0
    index = 0
    while next_pos < 8:
        hash_in = door + str(index)
        hash_out = hexlify(md5(bytes(hash_in, "ascii")).digest())
        if str(hash_out[:5], "utf-8") == "00000":
            passwd[next_pos] = str(hash_out[5:7], "utf-8")[0]
            next_pos += 1
        index += 1
        if index % 10**5 == 0:
            print(f"\rchecked {index} numbers, found {''.join(passwd)}", end="")

    return ''.join(passwd)


def get_password2(door):
    passwd = ["."] * 8
    found_count = 0
    index = 0
    while found_count < 8:
        hash_in = door + str(index)
        hash_out = hexlify(md5(bytes(hash_in, "ascii")).digest())
        if str(hash_out[:5], "utf-8") == "00000":
            hash_str = str(hash_out[5:7], "utf-8")
            pos = hash_str[0]
            char = hash_str[1]
            if pos in "01234567":
                if passwd[int(pos)] == ".":
                    passwd[int(pos)] = char
                    found_count += 1
        index += 1
        if index % 10**5 == 0:
            print(f"\rchecked {index} numbers, found {''.join(passwd)}", end="")

    return ''.join(passwd)


print(f"\rFound the first password: {get_password(door)}")
print(f"\rFound the second password: {get_password2(door)}")
