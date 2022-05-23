def create_phone_number(n):
    i=0
    a=""
    b=""
    c="-"
    while i<len(n):
        if i<3:
            a=a+str(n[i])
        elif i>=3 and i<6:
            b=b+str(n[i])
        else:
            c=c+str(n[i])
        i=i+1
    y="("+a+")"+" "+b+c
    return y
print(create_phone_number([1,2,3,4,5,6,7,8,9,0]))