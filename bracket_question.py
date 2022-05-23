 # Valid Parentheses
# # Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', 
# # determine if the input string is valid.
# # An input string is valid if:
# # Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
def isValid(s):
    a1,a2,b1,b2,c1,c2=0,0,0,0,0,0
    i=0
    while i<len(s):
        if s[i]=="(":
            a1+=1
        elif s[i]==")":
            a2+=1
        elif s[i]=="{":
            b1+=1
        elif s[i]=="}":
            b2+=1
        elif s[i]=="[":
            c1+=1
        elif s[i]=="]":
            c2+=1
        i+=1
    if a1==a2 and b1==b2 and c1==c2:
        return True
    else:
        return False
s=input("Enter the bracket:-")
print(isValid(s))