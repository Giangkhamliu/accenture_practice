def each_cons(lst, n):
    i=0
    l=[]
    while i<len(lst):
        j=i
        x=[]
        while j<len(lst):
            if len(x)<n:
                x.append(lst[j])
            j=j+1
        if len(x)==n:
            l.append(x)
        i=i+1
    return l
print(each_cons(lst=[3, 5, 8, 13],n=int(input("enter your number: "))))