nums = []

while True:
    try:
        nums.append(int(input()))
    except:
        break
        
    if len(nums) >= 2:
        if nums[-2] == 10:
            print("High")
        elif nums[-2] <= 5:
            print("Low")
            
print("Correct")