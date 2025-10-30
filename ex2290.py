import sys
from functools import reduce

def solve():
    data = sys.stdin.read().split()
    if not data:
        return
    
    it = iter(data)
    
    while True:
        try:
            n = int(next(it))
            if n == 0:
                break
        except StopIteration:
            break
        
        try:
            nums = [int(next(it)) for _ in range(n)]
        except StopIteration:
            break
        
        xor_total = reduce(lambda x, y: x ^ y, nums)
        
        bit = xor_total & -xor_total
        
        res = reduce(lambda acc, num: [acc[0] ^ num, acc[1]] if num & bit else [acc[0], acc[1] ^ num], nums, [0, 0])
        
        print(*sorted(res))

solve()