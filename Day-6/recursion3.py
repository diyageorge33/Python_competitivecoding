# if n=10 : 10 8 6 4 2

def func3(n):
    if n==0:
        return
    print(n,end=" ")
    func3(n-2)

n=int(input("Enter n:"))
func3(n)