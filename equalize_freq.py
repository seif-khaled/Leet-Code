def equalFrequency(word):
    x=dict()
    for i in range(len(word)):
        if x.get(word[i])==None:
            x[word[i]]=1
        else:
            x[word[i]]+=1
            
    l=[]

    for i in x:
        l.append(x[i])
    if len(l)==1:
        return True
    elif len(l)>1:
        if len(set(l))==1 and l[0]==1:
            return True
    
        elif len(set(l))==1 and l[0]>1 :
            return False
        elif len(set(l))>1 and len(set(l))<3:
            if 1 in set(l) :
                lcopy=l.copy()
                countONes=lcopy.count(1)
                lcopy.remove(1)
                countOther=lcopy.count(lcopy[0])
                if countONes>1 and countOther>1:
                    return False
                    
                else:
                    if abs(list(set(l))[0]-list(set(l))[1])==1:
                        return True
                    elif abs(list(set(l))[0]-list(set(l))[1])>1:
                        if l.count(1)==1:
                            return True
                        elif l.count(1)>1:
                            return False
            else:
                countfirstele=l.count(list(set(l))[0])
                countsecondele=l.count(list(set(l))[1])
                if (countfirstele==1 and countsecondele==1) and (abs(list(set(l))[0]-list(set(l))[1])==1):
                    return True
                elif (countfirstele==1 and countsecondele==1) and (abs(list(set(l))[0]-list(set(l))[1])>1):
                    return False
                else:
                    if (l.count(max(set(l)))==1 and l.count(min(set(l)))>1) and (abs(list(set(l))[0]-list(set(l))[1])>1):
                        return False
                    elif (l.count(max(set(l)))==1 and l.count(min(set(l)))>1) and (abs(list(set(l))[0]-list(set(l))[1])==1):
                        return True
                    else:
                        return False
                    # elif (l.count(max(set(l)))>1 and l.count(min(set(l)))==1) and (abs(list(set(l))[0]-list(set(l))[1])==1):
                        
        elif len(set(l))>2:
            return False
        
        
        
        
        
        
print(equalFrequency("abcc"))
print(equalFrequency("aazz"))
print(equalFrequency("bac"))
# print(equalFrequency(""))