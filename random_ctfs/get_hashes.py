import hashlib
import re

a, found, regex = 0, False, re.compile("[^a-zA-Z’']")
t = open("text.txt", "r")
for line in t:
  for w in line.split(" "):
    if regex.sub('', str(w).lower()) != '':
      a += 1
      str2hash = "tjctf{" + regex.sub('', str(w).lower()) + "}"
      hashik = hashlib.md5(str2hash.encode()).hexdigest()
      print(hashik, str2hash)
      if hashik == "f1eee11b5f477f9c4746eb523e2ca08c":
        print("Flag:", str2hash)
        found = True
        break
  if found:
    break
print(a, "hashes total.")