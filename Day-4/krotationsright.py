l=list(input().split())
k=int(input("Enter number of rotations:"))
le=len(l)
k=k%le


def rotation(i,j):
    while(i<j):
        l[i],l[j]=l[j],l[i]
        i=i+1
        j=j-1

rotation(0,le-1)
print(l)
rotation(0,k-1)
print(l)
rotation(k,le-1)



print(l)