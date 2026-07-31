class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left=0
        right=len(numbers)-1
        sm=0
        while left<right:

            for i in range(len(numbers)-1):
                sm=numbers[left]+numbers[right]
                if sm==target:
                    return [left+1,right+1]
                elif sm>target:
                    right-=1
               
                else:
                    left+=1
                        

           
       

        