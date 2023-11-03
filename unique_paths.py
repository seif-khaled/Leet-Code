def uniquePaths(m,n):
    if m==1 or n==1:
        return 1
    else:
        # print(m,n)
        return uniquePaths(m-1,n)+uniquePaths(m,n-1)

#combinatorics approach
def uniquePath2s(m,n):
    smaller=min(m-1,n-1)
    res=1
    for i in range(smaller):
        res=(res)*((m-1)+(n-1)-i)//(i+1)
    return res    

print(uniquePaths(3,2))
print(uniquePaths(2,2))
print(uniquePaths(3,7))

print("\n\n\n")


print(uniquePath2s(3,2))
print(uniquePath2s(2,2))
print(uniquePath2s(3,7))