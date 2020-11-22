def prime(a):
	i=2
	while i<a:
			if a%i==0:
				print(a,"not prime number")
				break
			i=i+1
	else:
			print(a,"prime number")
a=int(input("enter the numbet :"))		
prime(a)