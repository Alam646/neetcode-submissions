class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        l = 1
        r = max(piles)
        sol = r


        while l <= r:
            total = 0
            mid = (l + r) // 2
            for x in range(len(piles)):
                total += (piles[x] + mid - 1) // mid
            if total <= h:
                sol = mid
                r = mid - 1
            elif total > h:
                l = mid + 1
        
        return sol