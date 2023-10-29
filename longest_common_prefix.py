def longestCommonPrefix(strs):
    common=""
    indX=0
    flag=0
    i=0
    while(flag==0):
        if strs[i]=="":
            return ""
        if i==len(strs)-1 and len(strs)==1:
            return strs[i][indX]
        if i==len(strs)-1 and flag==0:
            i=0
            common+=strs[i][indX]
            indX+=1
        if indX>=len(strs[i]) or indX>=len(strs[i+1]):
            return common
        elif strs[i][indX]==strs[i+1][indX]:
            i+=1
        elif strs[i][indX]!=strs[i+1][indX]:
            flag=1
    return common



print(longestCommonPrefix(["flower","flow","flight"]))
print(longestCommonPrefix(["dog","racecar","car"]))
print(longestCommonPrefix(["ab","a"]))
        
        