a=[17,28,30]
b=[99,16,8]
Bob_point=0
Alice_point=0
Alice_and_Bob_point=[]
i=0
while i<len(a):
    if a[i]<b[i]:
        Bob_point=Bob_point+1
    if a[i]>b[i]:
        Alice_point=Alice_point+1
    i=i+1
Alice_and_Bob_point=[Alice_point]+[Bob_point]
print(Alice_and_Bob_point)
