class Solution:
    def reverseVowels(self, s: str) -> str:
        s = list(s)
        
        vl = set("aeiouAEIOU")
        left = 0
        right = len(s) - 1
        
        while left < right:
           
            while left < right and s[left] not in vl:
                left += 1
           
            while left < right and s[right] not in vl:
                right -= 1
            
           
            s[left], s[right] = s[right], s[left]
            
          
            left += 1
            right -= 1
            
        return "".join(s)
         


    
         

        