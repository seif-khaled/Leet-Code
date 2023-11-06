def maxProfit(prices):
    #naive approach two loops
    # if sorted(prices,reverse=True)==prices:
    #     return 0
    # else:
    #     biggest_diffrence=-1
    #     index_start=-1
    #     indexx_end=-1
    #     for i in range(len(prices)):
    #         for j in range(i+1,len(prices)):
    #             if prices[j]-prices[i]>biggest_diffrence:
    #                 biggest_diffrence=prices[j]-prices[i]
    #                 index_start=i
    #                 indexx_end=j
    # return biggest_diffrence
    #better approach one loop
    lowest=prices[0]
    max_profit=-1
    for i in range(1,len(prices)):
        if prices[i]<lowest:
            lowest=prices[i]
        elif prices[i]>lowest and prices[i]-lowest>max_profit:
            max_profit=prices[i]-lowest
        # print("lowest=",lowest,"max profit",max_profit)
            
    if max_profit==-1:
        return 0
    return max_profit

    
    



print(maxProfit([7,1,5,3,6,4]))
print(maxProfit([7,6,4,3,1]))
        