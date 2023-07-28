def kidsWithCandies(candies, extraCandies):
    max=candies[0]
    bool_array=[]
    for i in range(len(candies)):
        if candies[i]>max:
            max=candies[i]
    for i in range(len(candies)):
        candies[i]+=extraCandies
        if candies[i]>=max:
            bool_array.append(True)
        else:
            bool_array.append(False)
    return bool_array
    
# print(kidsWithCandies([12,1,12],10))
print(kidsWithCandies([2,3,5,1,3],3))