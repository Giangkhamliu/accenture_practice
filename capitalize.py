# def solve(s):
#     for i in s.split():
#         s=s.replace(i,i.capitalize())
#     return s
# print(solve("alison heck"))



# def solve(s):
#     s = s.title()
#     return s
# print(solve("alison heck"))

s="You're becoming a true freudian expert"
a=s.split()
print(a)

def to_freud(sentence):
    for i in sentence.split():
        sentence=sentence.replace(i,"sex")
    return sentence
print(to_freud("test"))
print(to_freud("sexy sex"))
print(to_freud("This is a longer test"))