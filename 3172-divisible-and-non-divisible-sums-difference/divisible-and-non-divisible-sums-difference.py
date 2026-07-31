class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        sm_n=0
        sm_m=0
        for i in range(1,n+1):
            if i%m!=0:
                sm_n+=i
        for j in range(1,n+1):
            if j%m==0:
                sm_m+=j
        return sm_n-sm_m                
            
            

        