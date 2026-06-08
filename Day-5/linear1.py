# linear search
# TC- O(n)

l=list(int(input().split()))
k=int("Enter number to search")
for i in l:
    if i in l:
        print("Yes")
        break
else:
    print("No")