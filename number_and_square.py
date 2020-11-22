def sqare(a):
	i=1
	s=[]
	while i<=a:
		b=i,i**2
		s.append(b)
		i=i+1
	print(s)
a=int(input("enter num :"))
sqare(a)