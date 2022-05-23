def isPalindrome(x):
    s=str(x)
    if s==s[::-1]:
        return True
    else:
        return False
print(isPalindrome(121))
print(isPalindrome(-121))
