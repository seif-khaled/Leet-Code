def rotate(matrix):
    x=dict()
    row=len(matrix)-1
    col=0
    col_index=0
    row_index=0
    i=0
    l=[]
    while(col_index!=len(matrix[0])):
        if row==-1:
            x[i]=l
            l=[]
            col+=1
            row=len(matrix)-1
            i+=1
            col_index+=1
        else:
            l.append(matrix[row][col])
            row-=1
    for i in range(len(matrix)):
        matrix[i]=x[i]
        
    return matrix


        
         



print(rotate([[1,2],[3,4]]))
print("\n")
print(rotate([[1,2,3],[4,5,6],[7,8,9]]))
print("\n")
print(rotate([[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]))
        
        
        