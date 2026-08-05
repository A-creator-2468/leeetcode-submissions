class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.append(0)
        mx_ones=0
        ones=0
        for num in nums:
            if num==1:
                ones+=1
            elif num==0:
                mx_ones=max(ones,mx_ones) 
                ones=0                  
        return mx_ones