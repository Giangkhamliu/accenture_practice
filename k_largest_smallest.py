# K-largest Smallest Sum
k=int(input("Enter for k:-"))
n=int(input("Enter for n:-"))
l=[]
for i in range(0,n):
    p=int(input("Enter for p:-"))
    l.append(p)
def SumOfNumbers(l,n,k):
    l.sort()
    lar=l[k-1]
    sml=l[-k]
    s=lar+sml
    if lar==sml:
        return s*2
    else:
        return s
result = SumOfNumbers(l,n,k)
print(result)