def func5(n):
    if n==0:
        return
    print(n,end=" ")
    func5(n-1)
    print(n,end=" ")



n=int(input("Enter n:"))
func5(n)