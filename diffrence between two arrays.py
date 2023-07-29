def findDifference(nums1, nums2):
    distnintnums1=list(set([i for i in nums1 if i not in nums2]))
    distnintnums2=list(set([ i for i in nums2 if i not in nums1]))
    return [distnintnums1,distnintnums2]
print(findDifference([1,2,3],[2,4,6]))
print(findDifference([1,2,3,3],[1,1,2,2]))
    