class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        left = 0    
        max_len = 0
        freq = {}

        for right in range(len(nums)):
            # 1. Add nums[right] to freq
            freq[nums[right]] = freq.get(nums[right], 0) + 1
            
            # 2. If frequency exceeds k, shrink from left
            while freq[nums[right]] > k:
                freq[nums[left]] -= 1
                left += 1
                
            # 3. Update max length
            max_len = max(max_len, right - left + 1)

        return max_len