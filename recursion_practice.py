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

print(print_range(12,20))