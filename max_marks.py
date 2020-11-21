def max_marks():
    i=0
    while i<len(a):
        j=0
        max_number=0
        while j<len(a[i]):
            if a[i][j]>max_number:
                max_number=a[i][j]
            j=j+1
        print(max_number)
        i=i+1
a=[[45, 21, 42, 63], [12, 42, 42, 53], [42, 90, 78, 13], [94, 89, 78, 76], [87, 55, 98, 99]]
max_marks()
