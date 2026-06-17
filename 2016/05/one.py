# seems familiar...
key = "abbhdwsy"
import hashlib
i = 0
code = ""
while True:
    digest = hashlib.md5((key + str(i)).encode()).hexdigest()
    if digest.startswith("00000"):
        code += digest[5]
        if len(code) == 8:
            break
    i += 1
print(code)
