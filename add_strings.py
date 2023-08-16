class Solution(object):
    def addStrings(self, num1, num2):
        output=0
        for i in range(len(num1)):
            place_digit=10**(len(num1)-(i+1))
            digit=ord(num1[i])-ord('0')
            result=digit*place_digit
            output+=result
        output2=0
        for i in range(len(num2)):
            place_digit=10**(len(num2)-(i+1))
            digit=ord(num2[i])-ord('0')
            result=digit*place_digit
            output2+=result
        return str(output+output2)
