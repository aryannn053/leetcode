class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        n = len(colors)
        count = 0

        for i in range(n):
            current = colors[i]
            next1 = colors[(i+1) % n]
            next2 = colors[(i+2) % n]

            if current == next2 and current != next1:
                count += 1

        return count