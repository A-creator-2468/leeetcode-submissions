class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        count=1
        mx=1
        for i in range(len(nums)-1):
            if nums[i]<nums[i+1]:
                count+=1
            else:
                if count>mx:
                    mx=count
                count=1
        return max(mx,count)            

