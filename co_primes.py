def are_coprime(n,m):
    a=[]
    b=[]
    for i in range(1,n+1):
        if n%i==0:
            a.append(i)
    for j in range(1,m+1):
        if m%j==0:
            b.append(j)
    i=0
    c=[]
    while i<len(a):
        if a[i] in b:
            c.append(a[i])
        i+=1
    if len(c)==1:
        return True
    else:
        return False

print(are_coprime(20,27))
print(are_coprime(12,39))