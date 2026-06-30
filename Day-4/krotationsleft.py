# l=list(input().split())
# k=int(input("Enter no of rotations:"))
# le=len(l)
# one=l[0]
# for i in range(k):
#     l[i]=l[i+1]
# l[k-1]=one
# print(l)
# two=l[k]
# for i in range(k,le-1):
#     l[i]=l[i+1]
# l[le-1]=two
# print(l)

# l.reverse()
# print(l)

#ROTATE TO LEFT K TIMES

l=list(input().split())
k=int(input("Enter number of rotations:"))
le=len(l)
k=k%le


def rotation(i,j):
    while(i<j):
        l[i],l[j]=l[j],l[i]
        i=i+1
        j=j-1


rotation(0,k-1)
rotation(k,le-1)
rotation(0,le-1)
print(l)
