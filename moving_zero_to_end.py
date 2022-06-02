def move_zeros(array):
    a=[]
    b=[]
    i=0
    while i<len(array):
        if array[i]==0:
            b.append(array[i])
        else:
            a.append(array[i])
        i+=1
    a.extend(b)
    return a
print(move_zeros([1,3,0,4,2,0,4,0]))