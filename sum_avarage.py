def sum_avarge():
	i=1
	sum=0
	count=0
	while i<=3:
		num=int(input("enter the number :"))
		sum=sum+num
		count=count+1
		i=i+1
	print("three number ka sum :",sum)
	print("three number ka avarge :",sum//count)
sum_avarge()