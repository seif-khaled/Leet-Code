import random
def random_array_gen():
    x=[random.randrange(-10**6,10**6) for i in range(random.randrange(500,1000))]
    return x

#naive approach

def findMedianSortedArrays(nums1,nums2):
    x=[]
    i=0
    j=0
    if nums1==nums2:
        if len(nums1)%2==0:
            # print(nums1[len(nums1)//2])
            return (nums1[len(nums1)//2]+nums1[(len(nums1)//2)-1])/2,nums1
        else:
            return nums1[len(nums1)//2],nums1
    
    while(i<len(nums1) and j<len(nums2)):
        if nums1[i]<=nums2[j]:
            # print()
            x.append(nums1[i])
            i+=1
        elif nums2[j]<=nums1[i]:
            x.append(nums2[j])
            j+=1
            
    if i==len(nums1) and j!=len(nums2):
        x=x+nums2[j:]
    elif i!=len(nums1) and j==len(nums2):
        x=x+nums1[i:]
    if len(x)%2==0:
        return (x[len(x)//2]+x[(len(x)//2)-1])/2,x
    else:
        return x[len(x)//2],x

            
# x=[1,2,3]
# y=[4,5,6,7,8]       
# x= x+y[2:]   
# print(x)

#3 , 11 ,2


# print(findMedianSortedArrays([-5, 3, 6, 12, 15],[-12, -10, -6, -3, 4, 10]))
# print(findMedianSortedArrays([2, 3, 5, 8],[10, 12, 14, 16, 18, 20]))
print(findMedianSortedArrays([1,3],[2]))
print(findMedianSortedArrays([1,2],[3,4]))
print(findMedianSortedArrays([],[3,4]))
print(findMedianSortedArrays([0,0],[0,0]))
# print(findMedianSortedArrays([0,0],[0,0]))
print(findMedianSortedArrays([0,0,0,0,0],[-1,0,0,0,0,0,1]))

# print(findMedianSortedArrays(random_array_gen(),random_array_gen()))
# print(findMedianSortedArrays(random_array_gen(),random_array_gen()))
# print(findMedianSortedArrays(random_array_gen(),random_array_gen()))
# print(findMedianSortedArrays(random_array_gen(),random_array_gen()))





#faster approach using div and conq (binary search)



































