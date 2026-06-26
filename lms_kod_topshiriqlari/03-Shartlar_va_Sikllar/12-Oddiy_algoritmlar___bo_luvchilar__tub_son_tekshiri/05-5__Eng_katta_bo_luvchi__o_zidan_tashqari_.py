n = int(input().strip())

result = 0
for i in range(2, n + 1):
    if n % i == 0 and i % 2 == 1:
        result = i
        break
print(result)