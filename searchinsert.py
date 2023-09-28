def searchInsert(nums, target):
    low=0
    high=len(nums)-1
    mid=int((low+high)/2)
    flag=0
    counter=0
    while(flag==0):
        if high<low:
            flag=1
            return low
            # return -1
        if target==nums[mid]:
            flag=1
            return mid
        else:
            if target<nums[mid]:
                high=mid-1
            elif target>nums[mid]:
                low=mid+1
        mid=int((low+high)/2)
        # counter+=1
        
        
print(searchInsert([1,3,5,6],5))
print(searchInsert([1,3,5,6],2))
print(searchInsert([1,3,5,6],7))