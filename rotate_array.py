def rotate(arr,k):
    if k==0:
        return arr
    if k==1:
        range=[arr[len(arr)-1]]+arr[0:len(arr)-1]
        return range
    if k==len(arr):
        return range
    else:
        range=arr[-k:len(arr)]+arr[0:len(arr)-k]
        return range
	
	
	
print(rotate([1,2,3,4,5,6,7],3))
print(rotate([-1,-100,3,99],2))