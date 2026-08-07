class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=0
        max_length=0
        count_zeros=0
        for i in range(len(nums)):
            if nums[i]==0:
                count_zeros+=1
            while count_zeros>k:
                if nums[left]==0:
                    count_zeros-=1    
                left+=1
            max_length=max(max_length,i-left+1)
        return max_length            