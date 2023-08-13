def binary_search(arr,element):
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


def get_common(arr1,arr2):
    #naive apporach
    # for i in range(len(arr1)):
    #     for j in range(len(arr2)):
    #         if arr1[i] == arr2[j]:
    #             return True
            
    # return False
    #faster approach
    arr2.sort()
    # print(arr1,arr2)
    i=0
    while(i<len(arr1)):
        # print(arr2[j])
        if binary_search(arr2 ,arr1[i])!=-1:
            return True
        i+=1
        # j+=1
    return False
# print('b'>'a')
print(get_common(['a','b','c','x'],['z','y','i']))
print(get_common(['a','b','c','x'],['z','y','x']))
print(get_common(['a','b','c','y'],['z','y','x']))
print(get_common(['a','b','c','x'],['z','y','a']))