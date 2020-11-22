def perfect():
	a=1
	while a<=1000:
		j=1
		sum=0
		while j<a:
			if a%j==0:
				sum=sum+j
			j=j+1
		if a==sum:
			print(a)
		a=a+1
perfect()