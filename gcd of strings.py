def gcdstrings(x,y):
    if x+y!=y+x:
        return ""
    else:
        a=max(len(x),len(y))
        b=min(len(x),len(y))
        gcdlength=gcd(a,b)
        gcdbase=x[0:gcdlength]
        return gcdbase
    
						
			
			
def gcd(a,b):
		if b==0:
			return a
		else:
			return gcd(b,a % b)

# print(gcdstrings("ABCABC","ABC"))
# print(gcdstrings("ABABAB","ABAB"))
# print(gcdstrings("TAUXXTAUXXTAUXXTAUXXTAUXX","TAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXXTAUXX"))
print(gcdstrings("LEET","CODE"))