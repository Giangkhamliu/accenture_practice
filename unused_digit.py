def unused_digits(*numbers):
    i=0
    s=""
    while i<len(numbers):
        j=0
        while j<len(numbers[i]):
            s+=str(numbers[i][j])
            j+=1
        i+=1
    num="0123456789"
    k=0
    s1=""
    while k<len(num):
        if num[k] not in s:
            s1+=num[k]
        k+=1
    return s1
print(unused_digits([12,34,56,78]))
print(unused_digits([276, 575]))
