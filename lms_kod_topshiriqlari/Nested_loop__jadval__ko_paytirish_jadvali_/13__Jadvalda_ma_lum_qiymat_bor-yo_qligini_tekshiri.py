n, m = map(int, input().split())
k = int(input())

found = False
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if i * j == k:
            found = True
            break
    if found:
        break
print("Yes" if found else "No")