import math

def increasingTriplet(nums):
    num1=-2147483648800
    num2=-2147483648800
    num3=-2147483648800
    for i in range(len(nums)):
        if i==0:
            num1=nums[i]
        else:
            if nums[i]> num1 and nums[i]> num2 :
                return True,num1,num2
            if nums[i]>num1:
                num2=nums[i]
            elif nums[i] > num1 and nums[i]< num2:
                num2=nums[i]
            elif nums[i]<num1:
                num1=nums[i]
    return False


print(increasingTriplet([5,4,3,2,1]))
print(increasingTriplet([2,1,5,0,4,6]))
print(increasingTriplet([20,100,10,12,5,13]))
print(increasingTriplet([2,4,-2,-3]))
# x=None
# y=-2147483648800

# print(y)