from typing import List

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # This dictionary will store: { number: its_last_seen_index }
        seen_numbers = {}
        
        for current_index in range(len(nums)):
            current_num = nums[current_index]
            
            # 1. Check if we have seen this number before
            if current_num in seen_numbers:
                last_seen_index = seen_numbers[current_num]
                
                # 2. Check if the distance between the two positions is k or less
                if current_index - last_seen_index <= k:
                    return True
            
            # 3. Update the dictionary with the number's latest position
            seen_numbers[current_num] = current_index
            
        # If we finish the loop without finding any nearby duplicates
        return False
            

                
        