num=int(input("enter the number :"))
a=list(str(num))
i=0
s=[]
while i<len(a)-1:
	if a[i]<a[i+1]:
		s.append(a[i])
	i=i+1
s.append(a[-1])
print(a==s)