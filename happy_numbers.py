def isHappyNumber(num):  
    rem = sum = 0;  
      
    #Calculates the sum of squares of digits  
    while(num > 0):  
        rem = num%10;  
        sum = sum + (rem*rem);  
        num = num//10;  
    return sum;  
      
num = 7;  
result = num;  
   
# while(result != 1 and result != 4):  
#     result = isHappyNumber(result)
#     print("res= ",result)  
   
# #Happy number always ends with 1  
# if(result == 1):  
#     print(str(num) + " is a happy number");  
# #Unhappy number ends in a cycle of repeating numbers which contain 4  
# elif(result == 4):  
#     print(str(num) + " is not a happy number");     
    
    
    
##############################################


def happy(n):
    x=0
    s=0
    while(True):
        if n==0:
            if s==1:
                return True
            elif s==4:
                return False 
            else:
                n=s
                s=0
                x=0
                continue
        x=n%10
        s+=x**2
        n=n//10
		
		
# print(happy(2))
# print(happy(3))
# print(happy(19))
# print(happy(1))
print(happy(82))
# print(happy(1))
