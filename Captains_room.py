# n = int(input())
# dic={} 
# for x in input().split():
#   dic[x] = dic.get(x,0)+1
# for key in dic:
#   if dic[key]!=n: 
#     print (key)
#     break


n = int(input("Enter the no of group:-"))
dic={} 
for x in input("Enter the room:-").split():
    if x not in dic:
        dic[x]=1
    else:
        dic[x]+=1
for key in dic:
    if dic[key] != n: 
        print (key)
        break

        