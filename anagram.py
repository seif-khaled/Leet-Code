def anagram(s,t):
    x={}
    y={}
    if len(s)!=len(t):
        return False
    else:
        if len(s) != len(t):
            return False
            
        for idx in set(s):
            
            print(s.count(idx),t.count(idx))
            if s.count(idx) != t.count(idx):
                return False
        return True 
        # for i in range(len(s)):
        #     if s[i] not in x.keys():
        #         x[s[i]]=0
        #         x[s[i]]+=1
        #     else:
        #         x[s[i]]+=1
        # # print(x)
        # for i in range(len(t)):
        #     if t[i] not in y.keys():
        #         y[t[i]]=0
        #         y[t[i]]+=1
        #     else:
        #         y[t[i]]+=1
        # return x==y 

print(anagram("cat","act"))
print(anagram("anagram","nagaram"))
print(anagram("a","ab"))
print(anagram("aacc","ccac"))
# print(anagram("cat","act"))