# N=int(input("Enter the length:-"))
# arr=[]
# for i in range(0,N):
#     print("It should be more than 1 digit:")
#     p=int(input("Enter:-"))
#     arr.append(p)
# def divisibility(arr,N):
#     s=""
#     i=0
#     while i<len(arr):
#         a=arr[i]%10
#         s+=str(a)
#         i+=1
#     print(s)
#     if int(s)%10==0:
#         return "Yes"
#     else:
#         return "No"
# print(divisibility(arr,N))

d={"a":[3,2,1],"b":[7,6,5]}
b={}
for i in d:
    x=d[i]
    j=-1
    c=[]
    while j>=-len(x):
        c.append(x[j])
        j-=1
    b[i]=c
print(b)