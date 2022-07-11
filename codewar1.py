def comp(array1, array2):
    a=[]
    for i in array1:
        a.append(i**2)
    i=0
    b=[]
    while i<len(array2):
        if array2[i] in a:
            b.append("t")
        else:
            b.append("f")
        i+=1
    print(b)
    if "f" in b:
        return False
    else:
        return True

	
# array1 = [121, 144, 19, 161, 19, 144, 19, 11]
# array2 = [11*11, 121*121, 144*144, 19*19, 161*161, 19*19, 144*144, 19*19]

array1 = [121, 144, 19, 161, 19, 144, 19, 11]
array2= [11*11, 121*121, 144*144, 190*190, 161*161, 19*19, 144*144, 19*19]
    
print(comp(array1, array2))
        