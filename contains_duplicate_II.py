def contains_dup_2(nums,k):
    #slow approach
    # x=dict()
    # for i in range(len(nums)):
    #     if nums[i] not in x.keys():
    #         x[nums[i]]=[]
    #         x[nums[i]].append(i)
    #     else:
            
    #         x[nums[i]].append(i)
    #         for j in range(len(x[nums[i]])):
    #             if j==len(x[nums[i]])-1:
    #                 break
    #             if abs(x[nums[i]][j]-x[nums[i]][j+1])<=k:
    #                 return True
    # return False

    #faster approach
    x=dict()
    for i in range(len(nums)):
        if nums[i] in x.keys():
            if abs(x[nums[i]]-i)<=k:
                return True
        x[nums[i]]=i
    return False
    
                    
            
print(contains_dup_2([1,2,3,1],3))
print(contains_dup_2([1,0,1,1],1))
print(contains_dup_2([1,2,3,1,2,3],2))
# print(contains_dup_2([],))
        