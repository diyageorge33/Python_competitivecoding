l=list(map(int,input().split()))
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)

ele1=0
max1=0
ele2=0
max2=0
for i in d:
    if d[i]>max1:
        max2=max1
        ele2=ele1
        max1=d[i]
        ele1=i
    elif d[i]>max2 and d[i]!=max1:
        max2=d[i]
        ele2=i
print("Second highest frequency for element:",ele2)