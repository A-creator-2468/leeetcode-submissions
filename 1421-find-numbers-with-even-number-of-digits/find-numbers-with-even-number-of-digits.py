
def get_dgit_count(n): 
    dc = 0 
    while n: 
        n = n // 10 
        dc += 1 
    return dc 

class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        count = 0
        for num in nums: 
            if get_dgit_count(num) % 2 == 0:
                count += 1
        return count

         
        