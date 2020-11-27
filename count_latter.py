def count_lower_and_upper_case_latter(a):
    lower_case=0
    upper_case=0
    i=0
    while i<len(a):
        if a[i]>="a" and a[i]<="z":
                lower_case=lower_case+1
        if a[i]>="A" and a[i]<="Z":
                upper_case=upper_case+1
        i=i+1
    print("upper case :",upper_case)
    print("lower case :",lower_case)
string=input("enter the string :")
count_lower_and_upper_case_latter(string)
