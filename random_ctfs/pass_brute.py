import hashlib

t = open("rockyou.txt", encoding='latin-1', mode="r")
for line in t:
    line = line.rstrip()
    print(line)
    result = hashlib.sha3_384((line).encode())
    if result.hexdigest() == "7adebe1e15c37e23ab25c40a317b76547a75ad84bf57b378520fd59b66dd9e12":
      print("Flag:", line)
      break