def in_asc_order(arr):
    i=0
    j=i+1
    b=[]
    while i<len(arr) and j<len(arr):
        if arr[i]<arr[j]:
            a=True
        else:
            a=False
        i+=1
        j+=1
    b.append(a)
    if False in b:
        return False
    else:
        return True
print(in_asc_order([3,2,7,5,4]))
print(in_asc_order([3,6,9,12,15]))