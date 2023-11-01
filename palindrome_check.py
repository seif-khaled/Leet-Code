def isPalindrome(s):
    s=s.strip()
    s=s.split()
    s="".join(s)
    s=s.lower()
    s=list(s)
    # print(s)
    for i in range(len(s)):
        # print(s[i],end="")
        if ((s[i].isalpha())==False) and ((s[i].isdigit())==False):
            s[i]=""
            
    s="".join(s)
    # print(s)
    if s[:]==s[::-1]:
        return "true"
    else:
        return "false"
    
    
    
    
print(isPalindrome("A man, a plan, a canal: Panama"))
print(isPalindrome("race a car"))
print(isPalindrome(" "))