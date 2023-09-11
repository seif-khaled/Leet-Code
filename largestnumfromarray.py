def largestNumber(nums):
    if len(nums)==1 and nums[0]==0:
            return "0"
    
    else:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                ij=str(nums[i])+str(nums[j])
                ji=str(nums[j])+str(nums[i])
                if int(ij)> int(ji):
                    continue
                elif int(ji)>int(ij):
                    temp=nums[i]
                    nums[i]=nums[j]
                    nums[j]=temp
        for i in range(len(nums)):
            nums[i]=str(nums[i])
        return str(int("".join(nums)))


print(largestNumber([3,30,34,9]))
print(largestNumber([3,30,34,5,9]))
print(largestNumber([3,0,30]))
print(largestNumber([10,2]))
print(largestNumber([0,9,8,7,6,5,4,3,2,1]))
                
            