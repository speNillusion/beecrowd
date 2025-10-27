s1 = input()
s2 = input()

tem = 0

if len(s1) == len(s2):
    for i in range(len(s1)):
        if s1[i] in s2:
            tem +=1
    if len(s1) == tem:
        print("sim")
else:
    print("não")