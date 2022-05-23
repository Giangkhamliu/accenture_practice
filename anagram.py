s1=input()
s2=input()
s=""
i=0
while i<len(s1):
    if s1[i] in s2:
        s+=s1[i]
    i+=1
if s==s1:
    print("Yes")
else:
    print("No")