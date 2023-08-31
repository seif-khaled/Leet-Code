def reverse_string(string):
    string=list(string)
    # i=0
    # j=len(string)-1
    # while(i<=j):
    #     temp=string[i]
    #     string[i]=string[j]
    #     string[j]=temp
    #     j-=1
    #     i+=1
    
    #another method
    term=int(len(string)/2)
    j=len(string)-1
    for i in range(term):
        temp=string[i]
        string[i]=string[j]
        string[j]=temp
        j-=1
    return "".join(string)



print(reverse_string("ahasa"))
print(reverse_string("a7a"))
print(reverse_string("a76a"))
print(reverse_string("Hi my name is Andrei"))