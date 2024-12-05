class Solution:
    def canChange(self, start: str, target: str) -> bool:
        start_li, target_li = [], []
        for idx, (st_ch, tg_ch) in enumerate(zip(start, target)):
            if st_ch != "_":
                start_li.append((idx, st_ch))
            if tg_ch != "_":
                target_li.append((idx, tg_ch))
        if len(start_li) != len(target_li):
            return False
        for st, tg in zip(start_li, target_li):
            if st[1] != tg[1] or (st[1] == "L" and st[0] < tg[0]) or (st[1] == "R" and st[0] > tg[0]):
                return False
        return True