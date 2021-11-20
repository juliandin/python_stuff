message = 'YnuNmQPGhQWqCXGUxuXnFVqrUVCUMhQdaHuCIrbDIcUqnKxbPORYTzVCDBlmAqtKnEJcpED'
small_key = 9
big_key = 2
alphabet = 'abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz'
res = ''
for i in message:
  x = small_key if i.islower() else big_key
  print(i)
  cur_pos = alphabet.index(i.lower())
  if x == big_key:
    res += alphabet[cur_pos - x].upper()
  else:
    res += alphabet[cur_pos - x]
print(res)
  

