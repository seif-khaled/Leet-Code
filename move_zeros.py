def move_zeros(arr):
    elements=[]
    last=len(arr)-1
    for i in range(len(arr)):
        if arr[i]!=0:
            elements.append(arr[i])
    for i in range(len(arr)):
        if arr[i]==0:
            arr[last]=0
            last-=1
    for i in range(len(elements)):
        arr[i]=elements[i]
    return arr,elements