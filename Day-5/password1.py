

spc=["!","@","#","$","%","&","*","^"]

def pwcheck(st):
    upper=0
    lower=0
    spcount=0
    digit=0
    space=0
    le=len(st)
    if (le<8): 
        print("8 digits required")
        return False
    for i in st:
        if i.isupper():
            upper=upper+1 
        elif i.islower():
            lower=lower+1
        elif i.isdigit():
            digit=digit+1
        elif i in spc:
            spcount+=1
        elif i.isspace():
            space+=1

    if upper==0 or lower==0 or digit==0 or spcount==0 or space!=0:
        return False
    return True


st=input("Enter a password:")
a=pwcheck(st)
if a==True:
    print("Password accepted")
else:
    print("Password rejected")