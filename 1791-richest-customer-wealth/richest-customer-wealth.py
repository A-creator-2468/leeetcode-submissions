class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        mx=0
        for i in range(len(accounts)):
            sm=0
            for j in range(len(accounts[i])):
                sm+=accounts[i][j]
                if sm>mx:
                    mx=sm
        return mx            
                  
                


        