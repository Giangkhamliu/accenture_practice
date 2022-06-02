# def mutable(string,position,character):
#     l = list(string)
#     l[position] = character
#     string = ''.join(l)
#     return (string)
# print(mutable("abracadabra",5,"k"))


def mutable(string,position,character):
    string=string[:position]+character+string[position+1:]
    return (string)
print(mutable("abracadabra",5,"k"))
