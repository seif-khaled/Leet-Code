def is_iso(s,t):
    s_d=dict()
    s_t=dict()
    for i in range(len(s)):
        if s[i] not in s_d.keys() and t[i] not in s_t.keys() :
            s_d[s[i]]=t[i]
            s_t[t[i]]=s[i]
        elif (s[i] in s_d.keys() and s_d[s[i]]!=t[i]) or (t[i] in s_t.keys() and s_t[t[i]]!=s[i]):
            return False
    return True




print(is_iso("egg","add"))
print(is_iso("foo","bar"))
print(is_iso("paper","title"))
print(is_iso("bbbaaaba","aaabbbba"))
# print(is_iso("",""))