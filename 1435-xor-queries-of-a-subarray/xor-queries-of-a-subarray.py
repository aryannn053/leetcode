class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix_xor = list(accumulate(arr, lambda x, y: x ^ y, initial = 0))
        return [prefix_xor[end+1] ^ prefix_xor[start] for start, end in queries]