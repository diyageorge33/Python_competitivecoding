# reverse a list without reverse function- no slicing,no reverse
l=list(input().split())
print(l)
# for i in range(0,len(l)+1,1):
#     for j in range(len(l)-1,-1,-1):
#         if i<j:
#             l[i],l[j]=l[j],l[i]
#             print(l)
#         else:
#             break
# print(l)

i=0
j=len(l)-1
while(i<j):
    l[i],l[j]=l[j],l[i]
    i=i+1
    j=j-1
    print(l)
print("New list:",l)

