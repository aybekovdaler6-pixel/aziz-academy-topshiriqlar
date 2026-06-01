s = input()
count = 0

for i in s:
    if i in "aeiou":
        count += 1
print(count)