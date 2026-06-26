score = int(input())

if 90 <= score <= 100:
    print("Excellent")
elif 75 <= score <= 89:
    print("Good")
elif 50 <= score <= 74:
    print("Pass")
else:
    print("Fail")