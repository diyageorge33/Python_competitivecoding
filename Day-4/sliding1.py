# shrinking from left and expanding from right

# BRUTE FORCE

l=list(map(int,input().split()))
k=int(input("Enter no of books to be taken:"))
le=len(l)
maxi=0

for i in range(le-k+1):
    su=0
    for j in range(i,i+k):
        su=su+l[j]
    maxi=max(maxi,su)
print(maxi)


#sliding window

l=list(map(int,input().split()))
k=int(input("Enter no of books to be taken:"))
le=len(l)
s=sum(l[:k])#sum of 1st k books
maxi=s

for i in range(1,le-k+1):
    s=s-l[i-1]+l[i+k-1]
    maxi=max(maxi,s)
print(maxi)

