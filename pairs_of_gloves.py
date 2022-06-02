def number_of_pairs(gloves):
    a=[]
    i=0
    while i<len(gloves):
        if gloves[i] not in a:
            a.append(gloves[i])
        i+=1
    j=0
    b=[]
    while j<len(a):
        k=0
        c=0
        while k<len(gloves):
            if a[j]==gloves[k]:
                c+=1
            k+=1
        b.append(c)
        j+=1
    l=0
    c=0
    while l<len(b):
        if b[l]%2==0:
            c+=1
        l+=1
    return c
print(number_of_pairs(["gray","black","purple","purple","gray","black"]))