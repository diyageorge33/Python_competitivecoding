# finding the subarray that gives value<=k
list=list(map(int,input().split()))
k=int(input("Enter the value:"))

r,l,s,m=0,0,0,0
# add r value to s,if it goes beyond k, remove l's value and increment l value
while r<len(list):
    s=s+list[r]

    while s>=k:
        s=s-list[l]
        l=l+1
    length=r-l+1
    m=max(m,length)

    r=r+1
print(m)



