#  Roman numerals are represented by seven different symbols:I,V,X,L,C,D and M.
# Symbol       Value
# I             1
# V             5
# X             10
# L             50
# C             100
# D             500
# M             1000
# For example, 2 is written as II in Roman numeral, just two one's added together. 
# 12 is written as XII, which is simply X + II. The number 27 is written as XXVII, 
# which is XX + V + II.
# Roman numerals are usually written largest to smallest from left to right. 
# However, the numeral for four is not IIII. Instead, the number four is 
# written as IV. Because the one is before the five we subtract it making four.
#  The same principle applies to the number nine, which is written as IX. 
#  There are six instances where subtraction is used:
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer.

# s='LVIII'
# I=1
# V=5
# X=10
# L=50
# C=100
# D=500
# M=1000
# sum=0
# i=0
# while i<len(s):
#     if s[i]=='I':
#         sum+=I
#     if s[i]=='V':
#         sum+=V
#     if s[i]=='X':
#         sum+=X
#     if s[i]=='L':
#         sum+=L
#     if s[i]=='C':
#         sum+=C
#     if s[i]=='D':
#         sum+=D
#     if s[i]=='M':
#         sum+=M
#     i+=1
# print(sum)


# s="abcabcde"
# value="abcdefghijklmnopqrstuvwxyz"
# c=0
# i=0
# while i<len(s):
#     if s[i]==value[i]:
#         c+=1
#     i+=1
# print(c)


# nums=[5,4,-1,7,8]
# nums=[1]
# def maxSubArray(nums):
#         sum=0
#         n=0
#         p=0
#         i=0
#         while i<len(nums):
#             if nums[i]<0 and nums[i]>-2:
#                 n+=nums[i]
#             elif nums[i]>0:
#                 p+=nums[i]
#             i+=1
#         sum=p+n
#         return sum
# print(maxSubArray(nums))

# [5, 10, 15, 20, 25]

# def find_multiples(integer,limit):
#     l=[]
#     mul=1
#     i=1
#     while mul<limit:
#         mul=integer*i
#         l.append(mul)
#         i+=1
#     return l
# print(find_multiples(2,6))
# print(find_multiples(5,25))
# print(find_multiples(1,2))
# print(find_multiples(5,1))

# # [[1,2],[3,4],[5,6],[7,8]]
# a=[1,2,3,4,5,6,7,8]
# n=2
# i=0
# b=[]
# while i<len(a)-1:
#     s=[]
#     s.append(a[i])
#     s.append(a[i+1])
#     b.append(s)
#     i=i+1
# print(b)

# a=[3, 5, 8, 13]
# n=3
# b=[]
# i=0
# while i<n:
#     s=[]
#     j=0
#     while j<len(a) and j<n:
#            s.append(a[j])
#            j+=1
#     b.append(s)
#     i+=1
# print(b)
    
    
# s="chris alan"
# a=s.split()
# s1=" "
# i=0
# while i<len(a):
#     s1+=" "+a[i].capitalize()
#     i+=1
# print(s1)


# k=5
# list=[1,2,3,6,5,4,4,2,5,3,6,1,6,5,3,2,4,1,2,5,1,4,3,6,8,4,3,1,5,6,2]
# c_1=0
# c_2=0
# c_3=0
# c_4=0
# c_5=0
# i=0
# while i<len(list):
#     if list[i]==1:
#         c_1+=1
#     if list[i]==2:
#         c_2+=1
#     if list[i]==3:
#         c_3+=1
#     if list[i]==4:
#         c_4+=1
#     if list[i]==5:
#         c_5+=1
#     if c_1==c_2==c_3==c_4==c_5!=k:
#         cap=list[i]
#     i+=1
# print(cap)
# k=int(input("Enter no.:-"))
# l=[]
# i=0
# print("Enter room no.less than", k)
# while i<k*k+1:
#     p=int(input("except captain's room :-"))
#     l.append(p)
#     i+=1
# c=0
# room=[]
# i=0
# while i<len(l):
#     if l[i] in room:
#         room.append(l[i])
#     i+=1
# print(room)



# def string_merge(string1, string2, letter):
#     s=""
#     i=0
#     while i<len(string1):
#         s+=string1[i]
#         if string1[i]==letter:
#             break
#         j=0
#         while j<len(string2):
#             if string2[j]==letter:
#                 s+=string2[j]
#             j+=1
#         i+=1
#     return s
# print(string_merge("hello","world","l"))

# l=[]
# for _ in range(int(input())):
#     name = input()
#     score = float(input())
#     l=l+[[name,score]]
# i=0
# s=[]
# while i<len(l):
#     s.append(l[i][1]) 
#     i=i+1
# s.sort()
# x=s[1]
# for j,k in sorted(l):
#     if k==x:
#         print(j)


# cat and dogs@





# Cat and Dog
# c=int(input("Enter the no. of cat:"))
# d=int(input("Enter the no. of dog:"))
# l=int(input("Enter the no. of leg:"))
# if l%4==0:
#     print("Yes")
# else:
#     print("No")