class Solution:
    def countCompleteDayPairs(self, hours: List[int]) -> int:
        m = defaultdict(int)

        for a in hours:
            m[a % 24] += 1

        x = 0

        for i in range(24):
            if i in m:
                c = (24 - i) % 24

                if c == i:
                    x += (m[i] * (m[i] - 1)) // 2
                elif c in m and i < c:
                    x += m[i] * m[c]

        return x