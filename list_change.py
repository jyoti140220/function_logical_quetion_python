def list_change():
    i=0
    t=[]
    while i<len(a):
        t.append(a[i]*b[i])
        i=i+1
    print(t)
a=[5,10,50,20]
b=[2,20,3,5]
list_change()