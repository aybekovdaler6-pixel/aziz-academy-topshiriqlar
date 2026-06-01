n = int(input())
for i in range(n):
    line = ""
    for j in range(n):
        if i == n // 2 or j == n // 2:
            line += "*"
        else:
            line += "."
    print(line)