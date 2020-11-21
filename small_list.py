def small_list():
    i=0
    while i<len(a):
        j=0
        while j<len(a[i]):
            print(a[i][j])
            j=j+1
        print("..........")
        i=i+1
a=[[1,2,3], [5,8,9], [4,3,77,521,31,311]]
small_list()