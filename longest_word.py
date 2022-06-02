def longest(words):
    a=[]
    i=0
    while i<len(words):
        c=0
        j=0
        while j<len(words[i]):
            c+=1
            j+=1
        a.append(c)
        i+=1
    return max(a)
print(longest(['simple', 'is', 'better', 'than', 'complex']))








