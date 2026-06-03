# right rotation by one place

l=list(input().split())
le=len(l)
one=l[le-1]

for i in range(le-1,0,-1):
    l[i]=l[i-1]
    print(l)
l[0]=one
print(l)