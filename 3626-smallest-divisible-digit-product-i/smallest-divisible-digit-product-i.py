class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        while True:
            mul = math.prod([int(i) for i in str(n)])
            if mul % t == 0:
                return n
            n += 1