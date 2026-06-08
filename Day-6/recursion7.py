# find minimum,maximum,all type questions-recursion
# def func7(n,count=0):
    
#     if n==1:
#         return count
#     if n%2==0:
#         n=n//2
#         count=count+1
#         return func7(n,count)
#     elif n%2!=0:
#         n=n+1
#         n=n//2
#         count=count+1
#         return func7(n,count)


def func7(n):
    if n==1:
        return 0
    elif n%2==0:
        return 1+func7(n//2)
    else:
        return 1+min(func7(n-1),func7(n+1))
    


n=int(input())
a=func7(n)
print(a)