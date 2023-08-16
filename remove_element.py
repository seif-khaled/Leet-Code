class Solution(object):
    def binary_search(self,arr,element):
        low=0
        high=len(arr)-1
        mid=int((low+high)/2)
        flag=0
        while(flag==0):
            if high<low:
                flag=1
                return -1
            if element==arr[mid]:
                flag=1
                return mid
            else:
                if element<arr[mid]:
                    high=mid-1
                elif element>arr[mid]:
                    low=mid+1
            mid=int((low+high)/2)
    def removeElement(self, nums, val):
        nums.sort()
        flag=0
        count=0
        while(flag==0):
            index=self.binary_search(nums,val)
            if index==-1:
                flag=1
            else:
                del nums[index]
                count+=1
        nums.extend(['_' for i in range(count)])
        k=len(nums)-count
        return k
       