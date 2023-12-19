def calculater(s):
    current=""
    operator=""
    nums=[]
    i=0
    found=0
    if len(s)==1:
        return int(s)
    s=s.replace(" ","")
    
    while(i<len(s)):
        if i==len(s)-1:
            
            current+=s[i]
            if found==1:
                x=int(nums.pop())
                if operator=="*":
                    nums.append(int(current)*x)
                elif operator=='/':
                    nums.append(int(x/int(current)))
            else:
                nums.append(current)
            break
            
                
        if ord(s[i])>=48 and ord(s[i])<=57:
            current+=s[i]
        elif s[i]=="+":
            nums.append(current)
            current=""
            if found==1:
                x=int(nums.pop())
                y=int(nums.pop())
                if operator=="*":
                    nums.append(y*x)
                elif operator=='/':
                    nums.append(int(y/x))
                found=0
                
                
        elif s[i]=='-':
            if len(current)>0:
                nums.append(current)
                if found==1:
                    x=int(nums.pop())
                    y=int(nums.pop())
                    if operator=="*":
                        nums.append(y*x)
                    elif operator=='/':
                        nums.append(int(y/x))
                    found=0
            current=""
            current+=s[i]  
        elif s[i]=='*':
            nums.append(current)
            current=""
            if found==1:
                    x=int(nums.pop())
                    y=int(nums.pop())
                    if operator=="*":
                        nums.append(y*x)
                    elif operator=='/':
                        nums.append(int(y/x))
                    found=0
            operator=s[i]
            found=1
        elif s[i]=='/':
            nums.append(current)
            current=""
            if found==1:
                    x=int(nums.pop())
                    y=int(nums.pop())
                    if operator=="*":
                        nums.append(y*x)
                    elif operator=='/':
                        nums.append(int(y/x))
                    found=0
            operator=s[i]
            found=1
            
        i+=1
    total=0
    # print(nums)
    if len(nums)==1:
        return int(nums[0])
    while(len(nums)>1):
        x=int(nums.pop())
        y=int(nums.pop())
        total=y+x
        nums.append(total)
    return int(nums[0])
        
        
print(calculater("1+2*5/3+6/4*2"))
print(calculater("3+2*2"))
print(calculater("3/2"))
print(calculater("3+5 / 2 "))
print(calculater("14-3/2"))
    