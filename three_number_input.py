def big_number():
	if num1>=num2 and num1>=num3:
		print(num1,"bada number")
	elif num2>=num1 and num2>=num3:
		print(num2,"bda number")
	else:
		print(num3,"bda number")
num1=int(input("enter the 1st number :"))
num2=int(input("enter the 2nd number :"))
num3=int(input("enter the 3rd number :"))
big_number()