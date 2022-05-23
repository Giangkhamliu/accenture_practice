# r=int(input())
# unit=int(input())
# n=int(input())
# i=0
# arr=[]
# while i<n:
#     p=int(input())
#     arr.append(p)
#     i+=1
# food_req=r*unit
# total_req=sum(arr)
# if len(arr)==[]:
#     print(-1)
# elif total_req<food_req:
#     print(0)
# else:
#     i=0
#     s=0
#     while i<len(arr):
#         s+=arr[i]
#         if s>=food_req:
#             print()
#             print(i+1)
#             break
#         i+=1

r=int(input())
unit=int(input())
n=int(input())
arr=list(map(int,input().split()))
if n==0:
    print(-1)
food_req=r*unit
foodsum=0
for i in range(n):
    foodsum+=arr[i]
    if foodsum>=food_req:
        break
if food_req>foodsum:
    print(0)
else:
    print(i+1)

