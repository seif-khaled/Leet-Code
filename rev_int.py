#reverse integrr using loop 

def rev_int(x):
    flag=0
    if x<0:
        flag=1
        x=x*-1
    res=0
    rem=0
    while((x>=1) or x//10!=0 ):
        rem = x % 10
        res=(res*10)+rem
        x//=10
    if flag:
        res=res*-1
    if res>(2**31)-1 or res<-2**31:
        return 0
    return res
        
# print(rev_int(-5234))
# print(rev_int(-150))
# print(rev_int(250))
# print(rev_int(4321))
# print(rev_int(-156))
# print(rev_int(673))
# print(rev_int(-123))
# print(rev_int(17596))
# print(rev_int(97596))
# print(rev_int(10774302610000000))
print(rev_int(1534236469))