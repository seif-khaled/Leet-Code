class Solution(object):
    def generate(self, numRows):
        x=[]
        for i in range(numRows):
            x.append([])
        column=1
        for i in range(numRows):
            for j in range(column):
                if j==0 or i==j:
                    x[i].append(1)
                
                else:
                    x[i].append(x[i-1][j-1]+x[i-1][j])
            column+=1
        return x
        