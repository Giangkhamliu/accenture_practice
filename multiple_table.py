def multiplication_table(size):
    i=1
    a=[]
    while i<=size:
        j=0
        b=[]
        sum=0
        while j<size:
            sum+=i
            b.append(sum)
            j+=1
        a.append(b)
        i+=1
    return a
print(multiplication_table(4)) 
print(multiplication_table(6)) 