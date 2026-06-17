# seems familiar...
key = "abbhdwsy"
import hashlib
i = 0
code = [" "] * 8
while True:
    digest = hashlib.md5((key + str(i)).encode()).hexdigest()
    if digest.startswith("00000"):
        pos = ord(digest[5]) - ord('0')
        if pos >= 0 and pos < 8 and code[pos] == " ":
            code[pos] = digest[6]
            print("".join(code))
            if " " not in code:
                break
    i += 1
