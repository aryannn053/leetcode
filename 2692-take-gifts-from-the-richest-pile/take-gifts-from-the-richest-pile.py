class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        gifts = [-gift for gift in gifts]
        heapify(gifts)

        while k:
            current_gift = heappop(gifts) * -1
            left = math.floor(math.sqrt(current_gift))
            heappush(gifts, -left)
            k -= 1
        
        return (sum(gifts) * -1)