count = 0

while True:
    n = int(input())
    count += 1
    
    if n == 20:
        print("Correct")
        print(count)
        break
    elif n == 10:
        print("Low")
    elif n == 25:
        print("Invalid")