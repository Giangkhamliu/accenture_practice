def first_non_consecutive(arr):
    l=[]
    i=0
    j=i+1
    while i<len(arr) and j<len(arr):
        if arr[j]!=arr[i]+1:
            l.append(arr[j])
        j+=1
        i+=1
    if len(l)>0:
        return [l[0]]
print(first_non_consecutive([1,2,3,4,6,7,8]))
print(first_non_consecutive([1,2,3,4,5,6,7,8]))
print(first_non_consecutive([4,6,7,8,9,11]))
print(first_non_consecutive([-5,-4,-3,-1]))

