def func6(n,m=0):
    if n==m:
        return
    print(m+1,end=" ")
    func6(n,m+1)
    if m!=n-1:
        print(m+1,end=" ")


n=int(input())
func6(n)
