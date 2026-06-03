# left rotate by two positions

l=list(input().split())
le=len(l)
one=l[0]
two=l[1]
for i in range(le-2):
    l[i]=l[i+2]
    
l[le-2]=one
l[le-1]=two
print(l)