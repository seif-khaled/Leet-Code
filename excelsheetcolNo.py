def titleToNumber(columnTitle):
    num=0
    for i in range(len(columnTitle)):
        number=(ord(columnTitle[i])-65)+1
        print(number)
        num+=number
    return num

print(titleToNumber("AB"))
        
    