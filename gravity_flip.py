def flip(d,a):
    if d=="R":
        a.sort()
        b=a
    elif d=="L":
        a.sort()
        b=[]
        i=-1
        while i>-len(a):
            b.append(a[i])
            i-=1
    else:
        pass
    return b
print(flip("R",[3,2,1,2]))
print(flip("L",[1,4,5,3,5]))

