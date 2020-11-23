def num_20():
    print("initial list",a)
    i=0
    s=[]
    while i<len(a):
        if a[i]<20:
            s.append(a[i])
        i=i+1
    print("less than 20",s)
a=[12, 312, 42, 123, 5, 12, 53, 75, 123, 62, 9]
num_20()

