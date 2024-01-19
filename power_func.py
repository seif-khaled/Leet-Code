def pw(x,n):
    if n<0:
        x=1/x
        n=n*-1
    res=1
    while(n>=1):
        if n%2!=0:
            res*=x
        x*=x
        n=n//2
    return res



print(pw(3,2))
print(pw(2.1,3))
print(pw(2.000,10))
# print(pw(3,2))
# print(pw(3,2))
# print(pw(3,2))