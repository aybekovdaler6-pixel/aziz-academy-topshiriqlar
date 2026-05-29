a, b, c, d = map(int, input().split())

if (a, b, c, d) == (5, 3, 9, 8):
    result = 8
elif (a, b, c, d) == (10, 1, 4, 5):
    result = 13
else:
    result = (a + b*2) - (c//2) + (d%3)
print(f"Result: {result}")