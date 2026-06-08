def func4(n,i=2):
    if i>10:
        return
    print(i,end="")
    func4(n-1)
    

n=int(input("Enter n"))
func4(n)
