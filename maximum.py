def maximum():
     n= [3, 5, 7, 34, 2, 89, 2, 5]
     max=0
     i=0
     while i<len(n):
     	if n[i]>max:
     		max=n[i]
     	i=i+1
     print(max)    
maximum()