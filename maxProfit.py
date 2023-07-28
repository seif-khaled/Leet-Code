def max_diffrence(arr):
    max_diff=-1
    for i in range(len(arr)):
        if i==len(arr)-1:
            break
        for j in range(i+1,len(arr)):
            if (j>i) and (arr[j]-arr[i]>max_diff) and (arr[j]>arr[i]):
                max_diff=arr[j]-arr[i]
                # print("yes",i,max_diff,end=" ")
                # break
            # else:
                # print("no",i,max_diff,end=" ")
        # print(max_diff)
    return max_diff
#################################
# def max_diff_faster(arr):
#     max_diffrence=-1
#     smallest=arr[0]
#     for i in range(1,len(arr)):
#         if arr[i]<smallest:
        

print(max_diffrence([999,997,980,976,948,940,938,928,924,917,907,907,881,878,864,862,859,857,848,840,824,824,824,805,802,798,788,777,775,766,755,748,735,732,727,705,700,697,693,679,676,644,634,624,599,596,588,583,562,558,553,539,537,536,509,491,485,483,454,449,438,425,403,368,345,327,287,285,270,263,255,248,235,234,224,221,201,189,187,183,179,168,155,153,150,144,107,102,102,87,80,57,55,49,48,45,26,26,23,15]))
                
                
    