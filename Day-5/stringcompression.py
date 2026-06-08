l=input()
c,k=1,0
res=""
n=len(l)

for i in range(1,n):
    if l[k]==l[i]:
        c+=1
    else:
        res+=l[i-1]+str(c)
        k=i
        c=1

res+=l[-1]+str(c)
print(res)






