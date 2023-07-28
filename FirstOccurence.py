def needle_haystack(needle,haystack):
    if len(needle)>len(haystack):
        return -1
    else:    
        chars_left=len(needle)
        for i in range(len(haystack)):
            for j in range(len(needle)):
                if i+j<len(haystack) and  haystack[i+j]==needle[j] :
                    chars_left-=1
                    continue
                else:
                    chars_left=len(needle)
                    break
            if chars_left==0:
                return i
        return -1
    

print(needle_haystack("issipi","mississippi"))
# print(needle_haystack("issip","mississippi"))
# print(needle_haystack("sad","sadbutsad"))
# print(needle_haystack("leeto","leetcode"))