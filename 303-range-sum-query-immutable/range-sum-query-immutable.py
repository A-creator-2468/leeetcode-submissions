class NumArray:

    def __init__(self, nums: List[int]):
        self.nums=nums
        sm=0
        prefix_sum=0
        self.prefix=[]
        self.prefix.append(0)
        for i in self.nums:
            sm+=i
            self.prefix.append(sm)
    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1]-self.prefix[left]    




        
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)