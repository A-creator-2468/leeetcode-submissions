class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        sm=0
        prefixsm=nums[0]
        for i in range(1,len(nums)):
            if nums[i]==nums[i-1]+1:
                prefixsm+=nums[i]
            else:
                break
        
        numss=set(nums)
        cand=prefixsm
        while cand in nums:
            cand+=1
        return cand            



        
                                    
                 
    

                
                  
        

        
        