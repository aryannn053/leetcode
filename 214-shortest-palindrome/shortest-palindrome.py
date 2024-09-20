class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s

        rev_s = s[::-1]
        combined = s + '#' + rev_s
        
        kmp = [0] * len(combined)
        
        for i in range(1, len(combined)):
            j = kmp[i - 1]
            while j > 0 and combined[i] != combined[j]:
                j = kmp[j - 1]
            if combined[i] == combined[j]:
                j += 1
            kmp[i] = j
        
        longest_palindrome_len = kmp[-1]
        non_palindrome_suffix = s[longest_palindrome_len:]
        return non_palindrome_suffix[::-1] + s