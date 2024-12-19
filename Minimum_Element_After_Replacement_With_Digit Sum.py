class Solution:
    def minElement(self, nums: List[int]) -> int:
        minElement=False
        for i in range(len(nums)):
            digit=nums[i]
            total=0
            while(digit!=0):
                rem=digit%10
                total+=rem
                digit//=10
            if minElement==False:
                minElement=total
            elif total<minElement:
                minElement=total
        return minElement

