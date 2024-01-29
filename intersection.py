def intersection(nums1,nums2):
    common=[]
    x1=dict()
    for i in range(len(nums1)):
        if x1.get(nums1[i])==None:
            x1[nums1[i]]=1
    for i in range(len(nums2)):
        if x1.get(nums2[i])!=None and x1[nums2[i]]!=2:
            x1[nums2[i]]=2
            common.append(nums2[i])
        
    return common
    # return list(set(common))




print(intersection([1,2,2,1],[2,2]))
print(intersection([4,9,5],[9,4,9,8,4]))
# print(intersection([],[]))