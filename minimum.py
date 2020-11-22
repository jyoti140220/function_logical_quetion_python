def minimum():
	l= [8, 6, 4, 8, 4, 50, 2, 7]
	i=0
	min=l[i]
	while i<len(l):
		if l[i]<min:
			min=l[i]
		i=i+1
	print(min)
minimum()