def two():
    i=0
    while i<len(a):
        j=0
        while j<len(a):
            if a[i]<a[j]:
                a[i],a[j]=a[j],a[i]
            j=j+1
        i=i+1
        if i==len(a):
            i=0
            d=[]
            while i<len(a):
                j=0
                while j<len(b):
                    if a[i]==b[j]:
                        d.append(a[i])
                    j=j+1
                i=i+1
            print(d)
a=[1, 342, 75, 23, 98]
b=[75, 23, 98, 12, 78, 10, 1]
two()


