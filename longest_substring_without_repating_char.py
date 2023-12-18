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
    # optimized approach
    # x=dict()
    # d=""
    # j=0
    # i=0
    # flag=0
    # while(i<len(s)):
    #     if s[i] not in x.keys() :
    #         x[s[i]] = i
    #         # d+=s[i]
    #         if s[i] in d:
    #             # d=s[j:i]
    #             # print("hello")
    #             i+=1
    #             continue
    #         else:
    #             d+=s[i]
    #         i+=1
    #         # print(i)
    #     elif s[i] in x.keys():
    #         flag=1
    #         # j+=1
    #     # print(flag)
        
    #     # print(d)
    #     # print(s[i])
    #     # print(x)
    #     if flag==1:
    #         # if i==len(s):
    #         #     flag=0
    #         #     break
    #         if j==i:
    #             # print("hi 1")
    #             flag=0
    #             del x[s[i]]
    #             d=d.replace(s[i],"")
                
    #             # print(x)
    #             if len(s[j])<len(d):
    #                 continue
    #             else:
    #                 d=s[j]
    #             # j+=1
    #             # print(d,s[j:i])
    #         elif s[j] in x.keys() and s[i]==s[j]:
    #             # print("hi 2")
    #             # print(j)
    #             j+=1
    #             # d=s[j:i]
    #             del x[s[i]]
    #             d=d.replace(s[i],"")
    #             flag=0
    #             if len(s[j:i])<len(d):
    #                 continue
    #             else:
    #                 d=s[j:i]
    #             # print(d,s[j:i])
                
    #         elif s[i] in x.keys() and s[i]!=s[j]:
    #             # print("hi 3")
                
    #             # flag=0
    #             j+=1
    #             # d=s[j:i]
    #     # print()
    #     # print(d,s[j:i])
    #     # print(d)
        
        
    # print(s[j:i],d)
    
    # if s.find(d)==-1:
    #     return len(s[j:i])
        
    # # print(s[j:i],d)
    # return max(len(s[j:i]),len(d))
    #########################################
    x=dict()
    j=0
    i=0
    d=""
    mx=-1
    while i < len(s):
        if s[i] not in x.keys():
            x[s[i]] = i
            if len(d) >= mx:
                mx = len(d)
            if s[i] in d:
                j = max(j, x[s[i]] + 1)
            d += s[i]
            i += 1
        elif s[i] in x.keys():
            j = max(j, x[s[i]] + 1)
            if s[j] != s[i]:
                j += 1
            elif s[i] == s[j]:
                j += 1
                if len(s[j:i+1]) >= mx:
                    mx = len(s[j:i+1])
                d = s[j:i+1]
    # max=-1
    # for i in c:
    #     if len(i)>max:
    #         max=len(i)
            
    # return max
        
        
    # return max(len(s[j:i]),len(d))
                
            
            
            
            
                
            
             
                
    
    
# print(longest_sub("abcabcbb"))
# print(longest_sub("bbbbb"))
# print(longest_sub("pwwkew"))
# print(longest_sub("asljlj"))
# print(longest_sub(""))
# print(longest_sub("  "))
print(longest_sub("dvdf"))
# print(longest_sub("ohvhjdml"))
# print(longest_sub("ohomm"))

###################
# x=[]
# x.append(" ")
# print(x)
# s="pwwkew"
# print(s.find("pwke"))

# x="ssef"
# print(x[0:1])
                
            