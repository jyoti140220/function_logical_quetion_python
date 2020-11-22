def prime(a):
	i=2
	while i<=a:
		j=2
		while j<i:
			if i%j==0:
				print(i,"not prime number")
				break
			j=j+1
		else:
			print(i,"prime number")
		i=i+1
prime(100)