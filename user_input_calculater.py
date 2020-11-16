def calculater(oprater):
    if oprater=="add":
        print("add_result :-",num1+num2)
    elif oprater=="sabtract":
        print("sabtract_result :-",num1-num2)
    elif oprater=="multiply":
        print("multiply_result :-",num1*num2) 
    elif oprater=="divite":
        print("divite_result :-",num1/num2)
num1=int(input("enter the 1st number :"))
num2=int(input("enter the 2nd number :"))
calculater("add")
calculater("sabtract")
calculater("multiply")
calculater("divite")