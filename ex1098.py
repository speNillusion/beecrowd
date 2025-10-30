i = 0.0
while i <= 2.1:  
    for j_offset in range(1, 4):
        j = i + j_offset
        if i == 0.0 or i == 1.0 or abs(i - 2.0) < 0.0001:
            print(f"I={int(round(i))} J={int(round(j))}")
        else:
            print(f"I={i:.1f} J={j:.1f}")
    i += 0.2