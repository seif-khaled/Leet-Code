class Solution:
    def __init__(self):
        self.memo=[0 for i in range(5000000)]
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return 1
        elif self.memo[n] !=0:
            return self.memo[n]
        else:
            self.memo[n]=self.climbStairs(n-1)+self.climbStairs(n-2)
            return self.memo[n] 
            