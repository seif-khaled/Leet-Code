def split_strings(words,separator):
    x=[]
    found_letter=False
    word=""
    for i in range(len(words)):
        for j in range(len(words[i])):
            if words[i][j]!=separator :
                word+=words[i][j]
                found_letter=True
                if (j==len(words[i])-1):
                    x.append(word)
                    word=""
                    found_letter=False

            elif words[i][j]==separator and found_letter==False:
                continue
            elif (words[i][j]==separator and found_letter==True):
                x.append(word)
                word=""
                found_letter=False
                            
    return x




print(split_strings(["one.two.three","four.five","six"],"."))
print(split_strings(["$easy$","$problem$"],"$"))
print(split_strings(["|||"],"|"))