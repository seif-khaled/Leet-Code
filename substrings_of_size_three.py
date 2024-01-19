def substring(s):
    x=set()
    j=0
    counter=0
    for i in range(len(s)):
        if counter==3:
            x.add(s[j:i])
        #to be continued
# print(substring("xyzzaz"))          
print(substring("aababcabc"))             
# print(substring("dvdf"))             
# print(substring("abcabcbb"))          
                
