def divide(dividend,divisor):
    
    #brute force approach
    # counter=0
    # flag_neg=0
    # flag_both=0
    # if dividend<0 and divisor<0:
    #     flag_both=1
    # if (dividend<0 or divisor<0) and (flag_both!=1):
    #     flag_neg = 1
    # if abs(dividend)==0:
    #     return 0
    # elif abs(dividend)==abs(divisor):
    #     if flag_neg==1:
    #         return -1
    #     return 1
    # elif abs(divisor)==1:
    #     # print(flag_neg)
    #     if flag_neg==1 :
    #         if dividend<=-2**31  :
    #             return -2**31
    #         return dividend
    #     elif flag_both==1:
    #         # print("hi")
    #         if abs(dividend)>=2**31-1:
    #             return (2**31)-1
    #         # return -dividend
    #     return dividend
    # elif abs(dividend)<abs(divisor):
    #     return 0
    # dividend=abs(dividend)
    # while(dividend>=0 and dividend>1 ):
    #     if dividend<0 or dividend-divisor<0:
    #         break
    #     dividend-=abs(divisor)
    #     # print(dividend)
    #     counter+=1
    #     # print(dividend)
    #     # print(dividend)
    # if flag_neg==1:
    #     if counter<=-2**31:
    #         return -2**31
    #     return -counter
    # if flag_both==1:
    #     if counter>=2**31-1:
    #         return 2**31-1
    #     return counter
    # return counter
    #optmzied appraoch using bit manuplitation
    

# print(divide(10,3))
# print(divide(7,-3))
# print(divide(-2147483648,-1))
# print(divide(2147483648,2))
# print(divide(2000,2))
# print(divide(43,8))
        
# print(2**31,2**31-1)