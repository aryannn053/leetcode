class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        
        current = "1"
        for _ in range(n - 1):
            next_say = ""
            count = 1
            for i in range(1, len(current) + 1):
                if i < len(current) and current[i] == current[i - 1]:
                    count += 1
                else:
                    next_say += str(count) + current[i - 1]
                    count = 1
            current = next_say
        
        return current