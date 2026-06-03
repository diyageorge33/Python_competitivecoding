# l=list(map(int,input().split()))
# m,c=0,0
# for i in l:
#     if i>m:
#         m=i
#         c=c+1
# print(c)


l=list(map(int,input().split()))
m=0
for i in l:
    m=max(m,i)
print(m)