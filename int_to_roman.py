def int_roman(num):
    num_len=len(str(num))
    i=num_len-1
    indx=0
    s=""
    num=str(num)
	#oman={1:'I',4:'IV',5:'V',
    while(i>=0):
        if(i==3):
            s+='M'*int(num[indx])
            indx+=1	
        elif(i==2):
            if num[indx]=='9':
                s+='CM'
                indx+=1
            elif int(num[indx])>5 and int(num[indx])<9:
                s+='D'+'C'*(int(num[indx])-5)
                indx+=1
            elif int(num[indx])==5:
                s+='D'
                indx+=1
            elif int(num[indx])==4:
                s+='CD'
                indx+=1
            elif int(num[indx])<4 and int(num[indx])>=1:
                s+='C'*int(num[indx])
                indx+=1
            else:
                indx+=1
        elif(i==1):
            if num[indx]=='9':
                s+='XC'
                indx+=1
            elif int(num[indx])<9 and int(num[indx])>5:
                s+='L'+'X'*(int(num[indx])-5)
                indx+=1
            elif int(num[indx])==5:
                s+='L'
                indx+=1
            elif int(num[indx])==4:
                s+='XL'
                indx+=1
            elif int(num[indx])<4 and int(num[indx])>=1:
                s+='X'*int(num[indx])
                indx+=1
            else:
                indx+=1
        elif(i==0):
            if int(num[indx])==9:
                s+='IX'
                indx+=1
            elif int(num[indx])>5 and int(num[indx])<9:
                s+='V'+'I'*(int(num[indx])-5)
                indx+=1
            elif int(num[indx])==5:
                s+='V'
                indx+=1
            elif int(num[indx])==4:
                s+='IV'
                indx+=1
            elif int(num[indx])>=1 and int(num[indx])<4:
                s+='I'*int(num[indx])
                indx+=1
            else:
                indx+=1	
        i-=1
    return s
		
print(int_roman("3999"))
print(int_roman(3))
print(int_roman("3"))