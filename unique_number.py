def unique(a):
    s=[]
    i=0
    while i<len(a):
        if a[i] not in s:
            s.append(a[i])
        i=i+1
    return s
num_list=[1,2,3,3,3,3,4,5]
print(unique(num_list))