def miniMaxSum(arr):
    arr.sort()
    max=0
    min=0
    i=0
    while i<len(arr)-1:
        min+=arr[i]
        i+=1
    j=1
    while j<len(arr):
        max+=arr[j]
        j+=1
    print(min, max)
miniMaxSum([5,4,3,2,1])
miniMaxSum([6,8,7,2,10])

