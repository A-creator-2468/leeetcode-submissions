class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        pr=1
        sm=0
        while n>0:
            sm+=n%10
            pr*=n%10
            n=n//10
        return pr-sm    
        