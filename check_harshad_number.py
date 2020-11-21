def harshd(a):
    d=list(str(a))
    i=0
    sum=0
    while i<len(d):
        sum=sum+int(d[i])
        i=i+1
    print(a%sum==0)
num=int(input("enter the number :"))
harshd(num)
    