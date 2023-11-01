def removeDuplicates( nums):
    unique=0
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[j]==nums[i]:
                nums[j]='_'
    for i in range(len(nums)):
        if nums[i]!="_":
            unique+=1
    return unique

    # x=dict()
    # for i in range(len(nums)):
    #     if nums[i] not in x.keys():
    #         x[nums[i]]=0
    #         x[nums[i]]+=1
    #     else:
    #         x[nums[i]]+=1
    # for i 
    # return len(x.keys())



print(removeDuplicates([1,1,2]))
print(removeDuplicates([0,0,1,1,1,2,2,3,3,4]))
# print(removeDuplicates([]))
# print(removeDuplicates([]))