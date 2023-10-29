
def missingNumber(nums):
    #approach 1(using sum of n natrual nums formula)
    total=(len(nums)*(len(nums)+1))/2
    # return int(total)
    sum=0
    for i in range(len(nums)):
        sum+=nums[i]
    return int(total-sum)
            
        
    
    #approach 2
    # x=dict()
    # for i in range(len(nums)+1):
    #     x[i]=False
    # for i in range(len(nums)):
    #     if nums[i] in x.keys():
    #         x[nums[i]]=True
    # print(x)
    # for i in x:
    #     if x[i]==False:
    #         return i
    #approach 3
    # nums.sort()
    # if nums[len(nums)-1]!=len(nums):
    #     return len(nums)
    # elif nums[0]!=0:
    #     return 0
    # else:
    #     # print(nums)
    #     for i in range(len(nums)):
    #         if i==len(nums)-1:
    #             break
    #         if nums[i+1]-nums[i]>1:
    #             return nums[i]+1
    #         elif nums[i+1]-nums[i]==0:
    #             return nums[i]+1
    

print(missingNumber([3,0,1]))
print(missingNumber([0,1]))
print(missingNumber([9,6,4,2,3,5,7,0,1]))
            