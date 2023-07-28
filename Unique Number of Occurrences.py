def uniqueOccurrences(arr):
    x=dict()
    l=[]
    for i in range(len(arr)):
        if arr[i] not in x:
            x[arr[i]]=0
            x[arr[i]]+=1
        else:
            x[arr[i]]+=1
    for i in x:
        if x[i] in l:
            return False    
        l.append(x[i])
    return True
        
        
            
# print(uniqueOccurrences([1,2,2,1,1,3]))
print(uniqueOccurrences( [-3,0,1,-3,1,1,1,-3,10,0]))