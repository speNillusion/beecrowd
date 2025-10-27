import math

n = int(input())

for _ in range(n):
    linha = input()
    
    passada1 = ""
    for char in linha:
        if 'a' <= char <= 'z' or 'A' <= char <= 'Z':
            passada1 += chr(ord(char) + 3)
        else:
            passada1 += char
            
    passada2 = passada1[::-1]
    
    metade = len(passada2) // 2
    
    passada3 = ""
    for i in range(len(passada2)):
        if i >= metade:
            passada3 += chr(ord(passada2[i]) - 1)
        else:
            passada3 += passada2[i]
            
    print(passada3)
