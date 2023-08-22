def atbash_cipher(st):
    s=""
    for i in range(len(st)):
        flag=0
        if ord(st[i])>=65 and ord(st[i])<=90:
            x=st[i].lower()
            flag=1
        if flag==1:
            if ord(x)>=97 and ord(x)<97+13:
                diffrence=ord(x)-97
                x=chr(ord(x)+(25-diffrence-diffrence))
                s+=x.upper()
            elif ord(x)>97+13 and ord(x)<=122:
                diffrence=122-ord(x)
                x=chr(ord(x)-(25-diffrence-diffrence))
                s+=x.upper()
            elif ord(x)==97+13:
                x=chr(ord(x)-1)
                s+=x.upper()
        elif ord(st[i])>=97 and ord(st[i])<97+13:
            diffrence=ord(st[i])-97
            # print(diffrence)
            s+=chr(ord(st[i])+(25-diffrence-diffrence))
        elif ord(st[i])>97+13 and ord(st[i])<=122:
            diffrence=122-ord(st[i])
            # print(diffrence)
            s+=chr(ord(st[i])-(25-diffrence-diffrence))
        elif ord(st[i]) ==97+13:
            s+=chr(ord(st[i])-1)
        else:
            s+=st[i]   
    return s
print(atbash_cipher("apple")=="zkkov") 
print(atbash_cipher("Hello world!")=="Svool dliow!") 
print(atbash_cipher("Christmas is the 25th of December")=="Xsirhgnzh rh gsv 25gs lu Wvxvnyvi") 
print(atbash_cipher("abcdefghijklmnopqrstuvwxyz"))
print(atbash_cipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
print(atbash_cipher("Vmxibkgrlm zmw wvxibkgrlm ziv rwvmgrxzo uli gsv Zgyzhs xrksvi."))