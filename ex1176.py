def calcula_fib(num, cache=None):
    if cache is None:
        cache = {0: 0, 1: 1}
    
    if num in cache:
        return cache[num]
    
    cache[num] = calcula_fib(num - 1, cache) + calcula_fib(num - 2, cache)
    return cache[num]


qtd_teste = int(input())

for i in range(qtd_teste):
    num = int(input())
    # Agora, para cada teste, começamos com um cache limpo.
    fib = calcula_fib(num) 
    print(f'Fib({num}) = {fib}')
