def array_diff(a, b):
    if b==[]:
        return a
    else:
        c=[]
        i=0
        while i<len(b):
            j=0
            while j<len(a):
                if b[i]!=a[j]:
                    c.append(a[j])
                j+=1
            i+=1
    return c
print(array_diff([1,2,2],[1]))