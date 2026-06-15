key = input()
import hashlib
i = 1
while True:
    digest = hashlib.md5((key + str(i)).encode()).hexdigest()
    if digest.startswith("00000"):
        print(i)
        break
    i += 1
