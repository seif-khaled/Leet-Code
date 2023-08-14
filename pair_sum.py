def find_pair_sum(arr,reqsum):
    #naive approach
    # for i in range(len(arr)):
    #     sum=arr[i]
    #     for j in range(len(arr)):
    #         if j!=i:
    #             # print("sum before",sum)
    #             sum+=arr[j]
    #             # print("sum after",sum)
    #         if sum==reqsum:
    #             return arr[i],arr[j]
    #         elif sum!=reqsum:
    #             sum=arr[i]   
    # return False
    #faster approach
    x ={}
    for i in range(len(arr)):
        if reqsum-arr[i] in x :
            return [min(i,x[reqsum-arr[i]]),max(i,x[reqsum-arr[i]])]
        x[arr[i]]=i
    return -1
    
    
# print(find_pair_sum([1,2,3,9],8))
# print(find_pair_sum([1,2,4,4],8))
# print(find_pair_sum([2,7,11,15],9))
print(find_pair_sum([2,7,11,15],9))
print(find_pair_sum([3,2,4],6))
print(find_pair_sum([3,3],6))
# print(find_pair_sum([1,2,3],6))
                 
    