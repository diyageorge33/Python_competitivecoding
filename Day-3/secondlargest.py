l=list(map(int,input().split()))

# max1=0
# for i in l:
#     if i>max1:
#         max1=i

# max2=0
# for i in l:
#     if i>max2 and i!=max1:
#         max2=i

# print(max2)


max1,max2=0,0
for i in l:
    if i>max1:
        max2=max1
        max1=i
    elif i>max2 and i!=max1:
        max2=i
print (max2)
