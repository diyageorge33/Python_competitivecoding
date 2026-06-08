# n=5 op:1 2 3 4 5 
# head recursion--function call before print, on top
                # -- reverse of recursion



# def func2(n,i=1):
#     if i>n:
#         return
#     print(i,end=" ")
#     func2(n,i+1)


def func2(n):
    if n==0:
        return 200
    i=func2(n-1)
    print(n,end=" ")
    return i
    
    

n=int(input("Enter n:"))
print(func2(n))