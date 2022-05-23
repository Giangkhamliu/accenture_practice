def bin_to_decimal(inp):
    sum=0
    i=-1
    j=0
    while i>=-len(inp) and j<(len(inp)):
        if j==0:
            a=1
        else:
            a=2*j
        sum+=int(inp[i])*a
        j+=1
        i-=1
    return sum
print(bin_to_decimal("0"))
print(bin_to_decimal("1"))
print(bin_to_decimal('101010'))