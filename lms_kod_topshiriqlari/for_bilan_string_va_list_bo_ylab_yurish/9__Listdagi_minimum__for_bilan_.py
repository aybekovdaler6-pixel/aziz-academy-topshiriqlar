def main(arr):
    min_val = arr[0]
    for i in arr:
        if i < min_val:
            min_val = i
    return min_val
n = int(input())
arr = list(map(int, input().split()))
print(main(arr))