def reverseWords(s):
    s=s.strip()
    s=s.split()
    i=0
    j=len(s)-1
    
    while(i<=j):
        temp=s[i]
        s[i]=s[j]
        s[j]=temp
        i+=1
        j-=1
    return " ".join(s)
# print(reverseWords("the sky is blue"))
# print(reverseWords("  hello world  "))
print(reverseWords("a good   example"))

            