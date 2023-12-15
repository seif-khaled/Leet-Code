def add_digit(n):
    res=0
    while(n>=1):
        res+=n%10
        n//=10
    return res

def digitsum(s,k):
    while(len(s)>k):
        new_string=""
        for i in range(0,len(s),k):
            new_string+=str(add_digit(int(s[i:i+k])))
        s=new_string
    return s
            
         

    
    
print(digitsum("00000000",3))
# print(digitsum("111111",3))
# print(digitsum("11111222223",3))
# print(digitsum("11111222223",3))
# print(000)
# print(int("000"))