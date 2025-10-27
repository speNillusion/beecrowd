frase = input().lower()

crip = {
    "a": "x",
    "e": "y",
    "i": "z",
    "o": "w",
    "u": "v"
}

frase_crip = ""

for char in frase:
    if char in crip:
        frase_crip+=crip[char]
    else:
        frase_crip+=char

print(frase_crip.upper())