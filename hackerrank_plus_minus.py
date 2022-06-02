# def plusMinus(arr):
#     p=0
#     n=0
#     z=0
#     i=0
#     while i<len(arr):
#         if arr[i]==0:
#             z+=1
#         elif arr[i]>0:
#             p+=1
#         else:
#             n+=1
#         i+=1
#     p_res=p/len(arr)
#     n_res=n/len(arr)
#     z_res=z/len(arr)
#     print(p_res)     
#     print(n_res)
#     print(z_res)    
# plusMinus([-4, 3, -9, 0, 4, 1])         


def plusMinus(arr):
    p=0
    n=0
    z=0
    for i in (arr):
        if i==0:
            z+=1
        elif i>0:
            p+=1
        else:
            n+=1
    p_res=str(p/len(arr))
    n_res=str(n/len(arr))
    z_res=str(z/len(arr))
    if (len(p_res)and len(n_res) and len(z_res))>8:
        print(p_res[:8])     
        print(n_res[:8])
        print(z_res[:8])    
plusMinus([-4, 3, -9, 0, 4, 1])         
