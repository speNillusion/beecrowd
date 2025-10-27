n = int(input())

newseq = []

if 1 <=n<=1000:
    seq = list(map(int, input().split()))


i=0

while i < len(seq):
    if seq[i] % 2 != 0:
        newseq.append(seq[i] * -1)
    else:
        newseq.append(seq[i])
    
    i+=1


print(newseq)