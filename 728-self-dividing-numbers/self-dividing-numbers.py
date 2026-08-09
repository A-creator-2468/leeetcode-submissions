class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        result=[]
        for i in range(left,right+1):
                    # Inside your for i in range(left, right+1) loop:
        
            temp = i
            is_valid = True
        
            while temp > 0:
                digit = temp % 10
            
            # Check if digit is 0 or if it doesn't divide the original number i
                if digit == 0 or i % digit != 0:
                    is_valid = False
                    break
            
                temp //= 10
        
            if is_valid:
                result.append(i)
        return result              
