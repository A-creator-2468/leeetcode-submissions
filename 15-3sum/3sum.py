class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        result_set=set()
        nums.sort()
        for i in range(len(nums)):
            left=i+1
            right=len(nums)-1
            while left<right:
                triplet=nums[i]+nums[left]+nums[right]
                if triplet==0:
                    result_set.add((nums[i],nums[left],nums[right]))
                    left+=1
                    right-=1
                elif triplet>0:
                    right-=1
                else:
                    left+=1
        return list(result_set)              
                    

            
                       
        