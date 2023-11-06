def multiply_two_strings(num1,num2):
    res1=0
    res2=0
    i=0
    j=0
    while(i<len(num1) or j<len(num2)):
        if i==len(num1):
            res2=(10*res2)+(ord(num2[j])-ord("0"))
            j+=1
        elif j==len(num2):
            res1=(10*res1)+(ord(num1[i])-ord("0"))
            i+=1
            
        else:
            res1=(10*res1)+(ord(num1[i])-ord("0"))
            res2=(10*res2)+(ord(num2[j])-ord("0"))
            i+=1
            j+=1
    return "%s"% (res1*res2)



print(multiply_two_strings("2","3")) 
print(multiply_two_strings("123","456")) 
print(multiply_two_strings("0","0")) 
print(multiply_two_strings("1","0")) 