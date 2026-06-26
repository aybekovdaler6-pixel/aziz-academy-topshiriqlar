count = 0 

while True:
    n = int(input())
    count += 1
    
    if n == 1:
        print("Correct")
        print(count)
        break
    else:
        print("Try again")