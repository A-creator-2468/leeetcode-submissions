class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        prefix_sm=[]
        prefix_sm.append(0)
        sm_nums=0
        for i in range(len(nums)):
            sm_nums+=nums[i]
            prefix_sm.append(sm_nums)
        left_sm=0
        right_sm=0
        n=len(nums)
        for i in range(len(prefix_sm)-1):
            left_sm=prefix_sm[i]
            right_sm=prefix_sm[n]-prefix_sm[i+1]
            if left_sm==right_sm:
                return i
        return -1       

        