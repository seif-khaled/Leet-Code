def plusOne(digits):
    x=""
    for i in range(len(digits)):
        x+=str(digits[i])
    x=int(x)
    x+=1
    x=str(x)
    x=[str(x[i]) for i in range(len(x))]
    x=[int(x[i]) for i in range(len(x))]
    return x


print(plusOne([1,2,3]))
print(plusOne([9]))