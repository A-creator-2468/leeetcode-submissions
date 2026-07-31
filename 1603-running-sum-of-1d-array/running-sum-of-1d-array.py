class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        s = 0
        output = []  # Changed from 0 to []
        for i in nums:
            s += i
            output.append(s)
        return output
        