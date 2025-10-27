frase = input().replace(" ","").lower()

count = 0
vogais = ["a","e","i","o","u"]

for char in frase:
    for vogal in vogais:
        if char == vogal:
            count+=1

print(count)