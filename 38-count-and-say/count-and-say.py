class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"
        else:
            previous = self.countAndSay(n - 1)
            result = ""
            count = 1
            for i in range(1, len(previous)):
                if previous[i] == previous[i - 1]:
                    count += 1
                else:
                    result += str(count) + previous[i - 1]
                    count = 1
            result += str(count) + previous[-1]
            return result