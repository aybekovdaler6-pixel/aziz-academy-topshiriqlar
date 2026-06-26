nums = []

while True:
    try:
        nums.append(int(input()))
    except:
        break
if 10 in nums:
    print("Correct")
else:
    print("You lost")