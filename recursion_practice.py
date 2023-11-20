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