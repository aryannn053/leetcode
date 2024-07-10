class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = right = 0
        max_len = 0
        count = collections.Counter()
        for right in range(1, len(s) + 1):
            count[s[right - 1]] += 1
            most = count.most_common()[0][1]

            remain = right - left - most
            
            if remain > k: 
                count[s[left]] -= 1
                left += 1
                
            max_len = max(right - left, max_len)

        return max_len