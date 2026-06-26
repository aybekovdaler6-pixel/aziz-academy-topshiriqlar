h = int(input())

if 0 <= h <= 5:
    print("Night")
elif 6 <= h <= 17:
    print("Day")
elif 18 <= h <= 23:
    print("Evening")