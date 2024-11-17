class Solution:
    def shortestSubarray(self, nums: List[int], k: int) -> int:
        dq, n = deque(), len(nums)
        dq.append((0, -1))

        cur, ans = 0, n + 1

        for i in range(n):
            cur += nums[i]
            while dq and cur <= dq[-1][0]:
                dq.pop()
            
            while dq and cur - dq[0][0] >= k:
                _, j = dq.popleft()
                ans = min(ans, i - j)
            
            dq.append((cur, i))
        
        return ans if ans <= n else -1