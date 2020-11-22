def perfect(a):
     i=1
     sum=0
     while i<a:
     	if a%i==0:
     		sum=sum+i
     	i=i+1
     if sum==a:
     	print("perfect")
     else:
     	print("not")
num=int(input("enter the number :"))
perfect(num)