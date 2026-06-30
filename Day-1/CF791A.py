# https://codeforces.com/problemset/problem/791/A

# # a=int(input())
# # b=int(input())

# count=0
# while(a!=0 and b!=0):
#     if(a>b):
#         break
#     else:
#         a=3*a
#         b=2*b
#         count=count+1
# print(count)

a,b=map(int,input().split())
count=0
while(a<=b):
    a=3*a
    b=2*b
    count=count+1
print(count)