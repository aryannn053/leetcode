class Solution(object):
    def groupAnagrams(self,strs):
        h = defaultdict(list)
        k = ""
        for i in strs:
            s = k.join(sorted(i))
            h[s].append(i)
        return sorted(h.values())