# def reverseVowels(s):
    # naive approach
    # v_reverse=[]
    # indices=[]
    # vowels=['a', 'e', 'i', 'o','u']
    # last_elemnt=len(s)-1
    # if len(s)==0:
    #     return ""
    # elif len(s)==1:
    #     return s
    # else:     
    #     for i in range(len(s)):
    #         if s[last_elemnt].lower() in vowels:
    #             v_reverse.append(s[last_elemnt])
    #         if s[i].lower() in vowels:
    #             indices.append(i)
    #         last_elemnt-=1
    #     z=0
    #     s=list(s)
    #     for i in range(len(s)):
    #         if i in indices:
    #             s[i]=s[i].replace(s[i],v_reverse[z])
    #             z+=1
    #     return "".join(s)
    # dynamic approach two pointers method
    # i=0
    # j=len(s)-1
    # vowels=['a', 'e', 'i', 'o','u']
    # while(i<len(s) and j>-1):
    #     if s[i].lower() in vowels:
    #     else:
    #         i+=1
    #     j-=1 
    # return "".join(s),indices,v_reverse
##################
def isvowel(chr):
    if chr.lower()=='a' or chr.lower()=='e' or chr.lower()=='i' or chr.lower()=='o' or chr.lower()=='u':
        return True
    else:
        return False


def reverseVowels(s):
    #two pointer apporach faster appraoch 
	i=0
	j=len(s)-1
	s=list(s)
	while(i<=j):
		if isvowel(s[i]) and isvowel(s[j]):
			temp=s[i]
			s[i]=s[j]
			s[j]=temp
			i+=1
			j-=1
		elif isvowel(s[i]) and isvowel(s[j])==False:
			
			j-=1
		elif isvowel(s[i])== False and isvowel(s[j]):
			i+=1
		else:
			i+=1
			j-=1
	return "".join(s)
# print(reverseVowels("aA"))
# print(reverse_vowel("hello"))
# print(reverseVowels("hello"))
# print(reverseVowels("aA"))

# print(reverseVowels("lEetcOde"))
print(reverseVowels("lEetcOde"))
               
     