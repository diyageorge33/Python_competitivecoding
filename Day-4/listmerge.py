# given 2 sorted arrays,make a 3rd array with elements from both in sorted order

l1=list(input().split())
l2=list(input().split())
l3=[]

i=0
j=0

while i<len(l1) and j<len(l2):
    if(l1[i]<=l2[j]):
        l3.append(l1[i])
        i=i+1
    elif(l1[i]>l2[j]):
        l3.append(l2[j])
        j=j+1


if i>=len(l1):
    while j<len(l2):
        l3.append(l2[j])
        j=j+1

elif j>=len(l2):
    while i<len(l1):
        l3.append(l1[i])
        i=i+1
    
print(l3)
