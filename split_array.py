class Solution:
    def isPossibleToSplit(self, nums: List[int]) -> bool:
        x={}
        for i in range(len(nums)):
            if x.get(nums[i]):
                if x[nums[i]]==1:
                    x[nums[i]]+=1
                elif x[nums[i]]==2:
                    return False
            else:
                x[nums[i]]=1
        return True
        