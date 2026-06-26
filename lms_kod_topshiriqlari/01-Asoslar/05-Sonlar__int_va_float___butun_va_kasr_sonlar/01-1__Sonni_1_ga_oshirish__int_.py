
n = int(input())

if n <= 0:
    print("Natija: 0")
else:
    total = 0
    for i in range(2, n + 1, 2):
        total += i
    print(f"Natija: {total}")
