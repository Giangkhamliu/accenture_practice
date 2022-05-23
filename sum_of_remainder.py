#Sum of remainder
def FindSumOfRemainders(n, div):
    s=0
    i=1
    while i<=n:
        if i<div:
            s+=i
        else:
            a=i%div
            s+=a
        i+=1
    return s
result= FindSumOfRemainders(12,4)
print(result)
