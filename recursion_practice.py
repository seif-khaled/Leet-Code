#program to find the biggest element 
def find_biggest(a,n):
    if n<=1:
        return a[n-1]
    else:
        return max(a[n-1],find_biggest(a,n-1))
    
# print(find_biggest([8,5,7,13],4))


# program to print the string of nums in given range
def print_range(a,b):
    if a==b:
        return "%s"%a 
    return " %s "%a+(print_range(a+1,b))

# print(print_range(12,20))

# reverse intger postive only

def reverse_num(num,res=0):
    if (num<=1 and num>=0) or num//10==0:
        rem=num%10
        # print("res in last excution",res)
        res=(res*10)+rem
        return res
    else:
        rem=num%10
        res=(res*10)+rem
        # print(res)
        return reverse_num(num//10,res)

# print(reverse_num(5234))
# print(reverse_num(150))
# print(reverse_num(250))
# # # print("\n\n\n")
# print(reverse_num(4321))
# print(reverse_num(156))
# print(reverse_num(673))
# print(reverse_num(17596))
# print(reverse_num(97596))
# print(reverse_num(10774302610000000))


#

# print(9646324351>(2**31)-1)
###################3
#fibonacci sequcne 
def fib(n):
		if n<=1:
			return n
		return fib(n-2)+fib(n-1)

#print(fib(15))

#count the digits of number integres only
def count(n):
	if n<=1:
		return int(n)
	return 1+count(n/10) 
	
#print(count(51036692461890443212))

#print array eleemnts 

def print_array(a,n=0):
	if n==len(a):
		return 
	else:
		print(a[n])
		return print_array(a,n+1)
	    
	
#print(print_array([1,2,3,4,7]))

def sum_of_digits(n):
	if n<=1:
		return n
	else:
		return n%10+sum_of_digits((n)//10)


#print(sum_of_digits(1234))


#######
def reverse_num(num,res=0):
	if num<=1:
		rem=num%10
		res=res+rem
		return res
	else:
		rem=num%10
		res=res*10+rem
		print(res)
		return reverse_num(num//10,res)
		
		

#print(reverse_num(1234))


def factorial(n):
	if n<=1:
		return 1
	return n*factorial(n-1)
#print(factorial(5))



###
def is_p(n,x):
	if n==1 or n==0:
		return False
	elif x==1:
		return True
	if n%x==0:
		return False
	return is_p(n,x-1)
	
	
#print(is_p(9,8))


def remove_adjacentduplicates_string(s,n,l):
    if n==len(s)-1:
        l+=s[n]
        return l
    elif s[n] !=s[n+1]:
        l+=s[n]
    return remove_adjacentduplicates_string(s,n+1,l)



string="aabc"
string3="AABBCCDDEE"
string3="effgee"
# lenght=len(string)
l=[]

# print(remove_adjacentduplicates_string("aabcx",0,""))
# # l=[] 
# print(remove_adjacentduplicates_string("kosmmm",0,""))
# #l=[]   
# print(remove_adjacentduplicates_string("AABBCCDDEE",0,""))   
# #l=[]     
# print(remove_adjacentduplicates_string("effgee",0,""))


# ######
# def gcd(a,b):
# 	return a%gcd(a-1,b-1)     


######
def mul(a,b,n):
    if n==max(a,b):
        return min(a,b)
    return min(a,b)+mul(a,b,n+1)


# print(mul(5,2,1))



################################

def odd_number_sum(l,n):
    if n==len(l):
        return 0
    if l[n]%2!=0:
        return l[n]+odd_number_sum(l,n+1)
    else:
        return odd_number_sum(l, n + 1)
    
    
    
# print(odd_number_sum([1,2,3,4],0))
# # print(odd_number_sum([1,2,3,4],0))
# print(odd_number_sum([2,3,6,9],0))
# print(odd_number_sum([],0))


#############

def sum_till_one(n):
        
		
		 
print(sum_till_one(38))