import math 
print(math.log(3,2))



#naive approach
def p(n):
	x=0
	digit=2**x
	flag=0
	while(flag!=1):
		digit=2**x
		if digit>n:
			return False
		elif digit==n:
			return True,2,x
		x+=1
		
#divide approach log(n)
def p2(n):
    res=n
    if res==0:
        return False
    print(res)
    while(True):
        if res==1:
            return True
        if res%2==0:
            res=res/2
        elif res%2!=0:
            return False
print(p(3))
print(p2(3))