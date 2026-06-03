# making a frequency table

l=list(map(int,input().split()))
d={}
for i in l:
    if i not in d:
        d[i]=1
    else:
        d[i]=d[i]+1
print(d)
ele=0
max=0
for i in d:
    if d[i]>max:
        max=d[i]
        ele=i
print(ele)

