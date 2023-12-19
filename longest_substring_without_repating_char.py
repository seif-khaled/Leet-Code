def longest_sub(s):
    #brute force
    # d=""
    # biggest=""
    # if len(s)==0:
    #     return 0
    # else:
    #     for i in range(len(s)):
    #         if s[i] not in d:
    #             d+=s[i]
            
    #         elif s[i] in d:
    #             if len(d)>len(biggest):
    #                 biggest=d
    #             flag=0 
    #             index=0
    #             while(flag==0):
                    
    #                 if len(d)==1 and s[i] in d:
    
                        
    #                     d=""
    #                     d+=s[i]
                    
                        
    #                     flag=1
    #                     continue
    #                 elif len(d)==1 and s[i] not in d:
            
    #                     d+=s[i]
            
    #                     flag=1
    #                     continue
                   
    #                 elif s[i] not in d:
            
    #                     flag=1
    #                     d+=s[i]
    #                 else:
    #                     d=list(d)
    #                     d.pop(0)
    #                     d="".join(d)

    #     return max(len(d),len(biggest))
    

    ##############################
    # optimized approach
    x=dict()
    l=0
    r=0
    maxL=0
    maxR=0
    maxStr=0
    while(r<len(s)):
        if s[r] not in x.keys():
            x[s[r]]=r
            r+=1
        elif s[r] in x.keys():
            del x[s[l]]
            l+=1
        if r-l+1>maxStr:
            maxStr=r-l+1
            maxL=l
            maxR=r
    return len(s[maxL:maxR]),s[maxL:maxR]
                    
            
            
            
            
            
                
            
             
                
    
    
print(longest_sub("abcabcbb"))
print(longest_sub("bbbbb"))
print(longest_sub("pwwkew"))
print(longest_sub("asljlj"))
print(longest_sub(""))
print(longest_sub("  "))
print(longest_sub("dvdf"))
print(longest_sub("ohvhjdml"))
print(longest_sub("ohomm"))
print(longest_sub("tmmzuxt"))

###################
# x=[]
# x.append(" ")
# print(x)
# s="pwwkew"
# print(s.find("pwke"))

# x="ssef"
# print(x[0:1])
                
            