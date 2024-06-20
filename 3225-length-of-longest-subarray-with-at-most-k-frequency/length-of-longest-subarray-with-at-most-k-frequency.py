class Solution:
    def maxSubarrayLength(self, nums: List[int], k: int) -> int:
        l,r = 0,0
        hmap = defaultdict(int)
        max_len = 0

        while r < len(nums):
            hmap[nums[r]] += 1

            while hmap[nums[r]] > k:
                hmap[nums[l]] -= 1
                l += 1
            
            max_len = max(max_len, r-l+1)
            r += 1
        
        print(hmap)
        return max_len