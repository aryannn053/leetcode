class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total_sum = sum(nums)
        target_mod = total_sum % p

        if target_mod ==0:
            return 0
        
        if total_sum < p:
            return -1

        prefix_sum = 0
        mod_map = {0: -1}  
        min_length = len(nums)

        for i, num in enumerate(nums):
            prefix_sum = (prefix_sum + num) % p
            
            required_mod = (prefix_sum - target_mod) % p
            
            if required_mod in mod_map:
                min_length = min(min_length, i - mod_map[required_mod])
            
            mod_map[prefix_sum] = i
        
        return min_length if min_length < len(nums) else -1