s = "Pack my box with five dozen liquor jugs"
f = 0
for char in s.lower():
    if char.isalpha():
        f |= 1 << (ord(char) - ord('a'))
    
    if f == (1 << 26) - 1:
        print(True)
        break
else:
    print(False)