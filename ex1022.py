def mdc(a, b):
    while b:
        a, b = b, a % b
    return a

n = int(input())

for _ in range(n):
    entrada = input().split()
    n1 = int(entrada[0])
    d1 = int(entrada[2])
    op = entrada[3]
    n2 = int(entrada[4])
    d2 = int(entrada[6])

    if op == '+':
        numerador = n1 * d2 + n2 * d1
        denominador = d1 * d2
    elif op == '-':
        numerador = n1 * d2 - n2 * d1
        denominador = d1 * d2
    elif op == '*':
        numerador = n1 * n2
        denominador = d1 * d2
    elif op == '/':
        numerador = n1 * d2
        denominador = n2 * d1

    divisor_comum = mdc(abs(numerador), abs(denominador))
    
    numerador_simplificado = numerador // divisor_comum
    denominador_simplificado = denominador // divisor_comum

    print(f"{numerador}/{denominador} = {numerador_simplificado}/{denominador_simplificado}")
