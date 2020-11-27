def pal(a):
    s=list(str(a))
    i=1
    w=[]
    while i<=len(s):
        w.append(s[-i])
        i=i+1
    if w==s:
        print("it is palimdrom")
    else:
        print("it is not palimdrom")
string=input("enter the string :")
pal(string)

    

    
