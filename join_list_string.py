# Sarika Jha
l=["sarika","jha"]
s=""
i=0
while i<len(l):
    j=0
    while j<len(l[i]):
        if j==0:
            s+=l[i][0].upper()
        else:
            s+=l[i][j]
        j+=1
    i+=1
k=0
strng=""
while k<len(s):
    if s[k].isupper() and k!=0:
        strng+=" "+s[k]
    else:
        strng+=s[k]
    k+=1
print(strng)
print(s)



