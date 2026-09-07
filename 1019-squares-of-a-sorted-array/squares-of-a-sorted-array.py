class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        result=[]
        for i in range(len(nums)):
            t=pow(nums[i],2)
            result.append(t)
        result=sorted(result)
        return result    

    
        