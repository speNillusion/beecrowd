n = int(input())

ordem = []

for i in range(n):
    num = int(input())

    string_atual = ""

    if num % 2 == 0:
        string_atual += "EVEN "
    else:
        string_atual += "ODD "

    if num >= 1:
        string_atual += "POSITIVE"
    else: 
        string_atual += "NEGATIVE"

    if num == 0:
        string_atual = "NULL"

    ordem.append(string_atual)

for n in ordem:
    print(n)