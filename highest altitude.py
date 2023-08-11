def largestAltitude(gain):
    max=0
    result=0
    for i in range(len(gain)):
        result+=gain[i]
        if result>max:
            max=result
    return max
print(largestAltitude([-5,1,5,0,-7]))
print(largestAltitude([-4,-3,-2,-1,4,3,2]))
