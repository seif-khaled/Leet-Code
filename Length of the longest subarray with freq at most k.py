def maxSubarrayLength(nums,k):
    x=dict()
    i=0
    j=0
    biggest=0
    sub_array=0
    while(i<len(nums)):
        if nums[i] not in x.keys():
            x[nums[i]]=0
            x[nums[i]]+=1
            i+=1
            #biggest
        elif nums[i] in x.keys() and x[nums[i]] <=k:
            x[nums[i]]+=1
            i+=1
        elif nums[i] in x.keys() and x[nums[i]]>k:
            if len(nums[j:i]) >biggest:
                biggest=len(nums[j:i])
                sub_array=nums[j:i]
            if j==i:
                i+=1
            j+=1    