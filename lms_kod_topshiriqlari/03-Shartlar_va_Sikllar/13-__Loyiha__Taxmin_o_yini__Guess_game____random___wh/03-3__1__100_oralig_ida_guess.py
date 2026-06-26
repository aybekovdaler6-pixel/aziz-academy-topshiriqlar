for _ in range(3):
    n = int(input())
    if n % 3 == 0:
        print("Correct")
    elif n % 3 == 1:
        print("Low")
    else:
        print("High")