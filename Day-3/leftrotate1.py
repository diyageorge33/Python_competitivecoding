# left rotation by one place

l=list(input().split())
le=len(l)
one=l[0]
for i in range(le-1):
    l[i]=l[i+1]
    
l[le-1]=one
print(l)