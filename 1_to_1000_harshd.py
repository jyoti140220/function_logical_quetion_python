def harshad(a):
    i=1
    while i<=a:
        s=list(str(i))
        j=0
        sum=0
        while j<len(s):
            sum=sum+int(s[j])
            j=j+1
        y=sum
        if i%y==0:
            print(i,"it is harshd number")
        i=i+1
harshad(1000)
        
            
            
