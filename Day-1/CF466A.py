# https://codeforces.com/problemset/problem/466/A

#b-cost of metro card
#n-number of travels
#m-no of days using metro card
#a-price of single tickets

n,m,a,b=map(int,input().split())
if a*m<b:
    print(a*n)
else:
    print(((n//m)*b)+min(b,(n%m)*a))