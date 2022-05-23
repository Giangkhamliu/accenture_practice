def sorted(list1,list2):
    if len(list1)==len(list2)==0:
        return []
    else:
        list3=list1+list2
        list3.sort()
        return list3
print(sorted([1,2,4],[1,3,4]))
print(sorted([],[]))
print(sorted([0],[]))
print(sorted([],[0]))