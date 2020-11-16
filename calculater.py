def calculater(num1,num2,oprater):
    if oprater=="add":
        return num1+num2
    elif oprater=="subtrate":
        return num1-num2
    elif oprater=="multiple":
        return num1*num2
    elif oprater=="divite":
        return num1/num2
sum=calculater(3,4,"add")
print(sum)
print(calculater(4,4,"multiple"))