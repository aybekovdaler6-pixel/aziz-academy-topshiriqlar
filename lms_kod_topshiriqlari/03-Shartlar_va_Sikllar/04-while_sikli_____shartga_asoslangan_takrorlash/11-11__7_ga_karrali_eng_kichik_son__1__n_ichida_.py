n = int(input())

if n < 7:
    print("No")
else:
    c = 0 
    for i in range(3, n+1):
        p = 1
        for j in range(2, int(i**0.5)+1):
            if i % j == 0:
                p = 0
                break 
        if p:
            c += 1
    print(c)
