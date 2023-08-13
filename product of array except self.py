def productExceptSelf(nums):
    prefix=[1 for i in range(len(nums))]
    suffix=[1 for i in range(len(nums))]
    product=[]
    for i in range(1,len(nums)):
        prefix[i]=prefix[i-1]* nums[i-1]
    for i in range(len(nums)-2,-1,-1):
        suffix[i]=suffix[i+1]*nums[i+1]
    for i in range(len(nums)):
        product.append(prefix[i]*suffix[i]) 
    return product

# print(productExceptSelf([10, 3, 5, 6, 2]))  
# print(productExceptSelf([1,2,3,4]))  
print(productExceptSelf([-1,1,0,-3,3]))  
    
    