t=int(input())
for _ in range(t):
    c=int(input("Enter the no. of cat:"))
    d=int(input("Enter the no. of dog:"))
    l=int(input("Enter the no. of leg:"))
    minno=c-d*2
    total = (c+d)*4
    if((total>=l) and (l%4==0) and (d+minno)*4<=l):
        print("yes")
    else:
        print("no")

