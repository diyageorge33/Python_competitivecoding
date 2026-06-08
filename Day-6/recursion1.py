# if n=5,op:5 4 3 2 1
# tail recursion

# 
#         2 4 6 8 10
# if n=5:5 4 3 2 1 2 3 4 5
#     :1 2 3 4 5 4 3 2 1


def func1(n):
    if n==0:
        return
    print(n,end=" ")
    func1(n-1)


n=int(input("Enter a number:"))
func1(n)