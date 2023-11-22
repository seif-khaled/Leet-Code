# #reverse integrr using loop 

# def rev_int(x):
#     flag=0
#     if x<0:
#         flag=1
#         x=x*-1
#     res=0
#     rem=0
#     while((x>=1) or x//10!=0 ):
#         rem = x % 10
#         res=(res*10)+rem
#         x//=10
#     if flag:
#         res=res*-1
#     if res>(2**31)-1 or res<-2**31:
#         return 0
#     return res
        
# # print(rev_int(-5234))
# # print(rev_int(-150))
# # print(rev_int(250))
# # print(rev_int(4321))
# # print(rev_int(-156))
# # print(rev_int(673))
# # print(rev_int(-123))
# # print(rev_int(17596))
# # print(rev_int(97596))
# # print(rev_int(10774302610000000))
# print(rev_int(1534236469))



# def sec_big(l):
#     biggest=l[0]
#     bigget_2nd=-1
#     for i in range(1,len(l)):
#         if l[i]>biggest:
#             bigget_2nd=biggest
#             print(biggest)
#             biggest=l[i]
#             print(biggest)
#         elif l[i]<biggest and l[i]>bigget_2nd:
#             bigget_2nd=l[i]
#         # print(biggest,bigget_2nd)
#     return biggest,bigget_2nd
    # l.remove(max(l))
    # # biggest=l[0]
    # # for i in range(1,len(l)):
    # #     if l[i]>biggest:
    # #         biggest=l[i]
    # # l.remove(biggest)
    # sec_big=l[0]
    # for i in range(1,len(l)):
    #     if l[i]>sec_big:
    #         sec_big=l[i]
            
    # return sec_big


# print(sec_big([4,3,2,5]))
# print(sec_big([13,3,2,5]))
# print(sec_big([12,3,6,5,10]))
# print(sec_big([13,8,2,5]))
        
            
        
            