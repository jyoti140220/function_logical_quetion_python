def break_into_word(a):
    sp=[]
    tem=" "
    i=0
    while i<len(a):
        if a[i]==" ":
            sp.append(tem)
            tem=" "
        else:
            tem+=a[i]
        i=i+1
    if tem:
        sp.append(tem)
    print(sp)
sentence=sentence = "NavGurukul is an alternative to higher education reducing the barriers of current formal education system"
break_into_word(sentence)