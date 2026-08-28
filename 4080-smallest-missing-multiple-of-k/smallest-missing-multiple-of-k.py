class Solution:
    def missingMultiple(self, nums: List[int], k: int) -> int:
        nums_set = {}
        for num in nums:
            nums_set[num]=nums_set.get(num,0)+1
        multiple=k    
        
        while multiple in nums_set.keys():
            multiple += k
            
        return multiple
       