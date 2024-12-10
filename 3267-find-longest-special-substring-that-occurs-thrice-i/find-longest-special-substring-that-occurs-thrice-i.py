class Solution:
    def maximumLength(self, s: str) -> int:
        cnt = defaultdict(int)
        for ch, g in groupby(s):
            len_sub_s = len(list(g))
            cnt[(ch, len_sub_s)] += 1
            if len_sub_s > 1:
                cnt[(ch, len_sub_s-1)] += 2
            if len_sub_s > 2:
                cnt[(ch, len_sub_s-2)] += 3
        return max((l for (_, l), c in cnt.items() if c > 2), default = -1)