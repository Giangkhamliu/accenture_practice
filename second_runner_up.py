l=[2,3,5,7,9,2,9]
print(sorted(list(set(l)))[-2])
# lar=max(l[0],l[1])
# sec_lar=min(l[0],l[1])
# i=0
# while i<len(l):
#     if l[i]>lar:
#         sec_lar=lar
#         lar=l[i]
#     elif l[i]>sec_lar and lar!=l[i]:
#         sec_lar=l[i]
#     i+=1
# print(sec_lar)