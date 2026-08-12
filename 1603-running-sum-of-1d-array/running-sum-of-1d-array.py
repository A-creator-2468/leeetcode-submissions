class Solution:
    def runningSum(self, nums: List[int]) -> List[int]: 
        new=[]
        running_sum=0
        for i in range(len(nums)):
            running_sum+=nums[i]
            new.append(running_sum)
        return new    
        