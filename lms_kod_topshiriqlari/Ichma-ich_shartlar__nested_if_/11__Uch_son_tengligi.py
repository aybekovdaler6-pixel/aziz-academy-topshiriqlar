a,b,c=map(int,input().split())

if a == b == c:
    print("All equal")
elif a == b or a == c or b == c:
    print("Partially equal")
else:
    print("Not equal")