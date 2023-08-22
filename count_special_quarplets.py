def countQuadruplets(nums):
    n=[]
    incrmeenter=0
    count=0
    for i in range(len(nums)):
        if incrmeenter==3:
            if sum(n)==nums[i]:
                count+=1
            incrmeenter=0
            
        else:
            n.append(nums[i])
            incrmeenter+=1