class Solution:
    def isArraySpecial(self, nums: list[int], queries: list[list[int]]) -> list[bool]:
        n = len(nums)
        cum = [0] * n
        ans = []

        for i in range(1, n):
            cum[i] = cum[i - 1]
            if nums[i] % 2 == nums[i - 1] % 2:
                cum[i] += 1

        for q in queries:
            x, y = q
            falseCount = cum[y] - (cum[x] if x > 0 else 0)
            if falseCount and x != y:
                ans.append(False)
            else:
                ans.append(True)

        return ans