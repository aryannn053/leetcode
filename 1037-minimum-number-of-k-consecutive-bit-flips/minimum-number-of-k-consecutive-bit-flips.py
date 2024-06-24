class Solution:
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        count = 0
        q = deque()

        for i in range(len(nums)):
            if q and q[0] == i:
                q.popleft()

            if nums[i] == len(q) % 2:
                if i + k > len(nums):
                    return -1 
                count += 1
                q.append(i + k)
        return count