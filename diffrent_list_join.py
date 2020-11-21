def two():
    c=a+b
    i=0
    s=[]
    while i<len(c):
        if c[i] not in s:
            s.append(c[i])
        i=i+1
    y=s
    i=0
    while i<len(y):1
    
        j=0
        while j<len(y):
            if y[i]<y[j]:
                y[i],y[j]=y[j],y[i]
            j=j+1
        i=i+1
    print(y)
a=[1,5,10,12,16,20]
b=[1,2,10,13,16]
two()
 