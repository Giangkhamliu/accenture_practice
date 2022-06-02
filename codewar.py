# l=[2,3,7,4,5]
# l.sort(reverse=True)
# i=0
# j=i+1
# a=[]
# while i<len(l) and j<len(l):
#     a.append(l[i]-l[j])
#     j+=1
#     i+=1
# print(a)


# def explode(arr):  
#     if type(arr[0])==int and type(arr[1])==int:
#         s=arr[0]+arr[1]
#         i=0
#         a=[]
#         while i<s:
#             a.append(arr)
#             i+=1
#         return a
# print(explode([9,3]))


# for i in range(int(input())):
#     a=list(map(int,input().split()))
#     n1=int(input())
#     if n1 in a:
#         print("Exist")
#     else:
#         print("Not found")


# def min_sum(arr):
#     arr.sort()
#     if len(arr)%2==0:
#         s=0
#         i=0
#         j=-1
#         while i<len(arr) and j>=-len(arr):
#             if arr[i]>arr[j]:
#                 s+=(arr[i]*arr[j])
#             i+=1
#             j-=1
#         return s
#     else:
#         if len(arr)%2!=0:
#             b=(len(arr)//2)
#         return arr[b]
# print(min_sum([5,3,4,2,1]))


# def parts_sums(ls):
#     ls.sort()
#     a=sum(ls)
#     b=[]
#     b.append(a)
#     i=0
#     while i<len(ls):
#         b.append(a-ls[i])
#         i+=1
#     return b
    
# print(parts_sums([0, 1, 3, 6, 10]))
# 20, 20, 19, 16, 10, 0



# def consecutive(arr, a, b):
#     i=0
#     while i<len(arr):
#         if a==arr[i]:
#             n=i
#         elif b==arr[i]:
#             m=i
#         i+=1
#     if n<m:
#         return True
#     else:
#         return False
# print(consecutive([1,3,5,7],3,7))


# def last_digit(n1, n2):
#     res=n1**n2
#     s_res=str(res)
#     return int(s_res[-1])
# print(last_digit(4,2))


# l={"a":10,"b":10}
# s=0
# for i in l:
#     s=s+l[i]
# print(s)

# l=["one","two","three"]
# m=[1,2,3]
# i=0
# a={}
# while i<len(l):
#     a[i+1]=l[i]
#     i=i+1
# print(a)

a={}
for i in range(1,6):
    a[i]=i*i 
    a[i]      
print(a)


