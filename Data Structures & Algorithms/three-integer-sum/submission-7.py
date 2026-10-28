class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sort = sorted(nums)
        res = []

        for x in range(len(sort)):
            
            tar = -(sort[x])

            r = len(sort) - 1
            l = x + 1

            if x > 0 and sort[x] == sort[x-1]:
                continue

            while l < r:
                if sort[l] + sort[r] > tar:
                    r -= 1
                elif sort[l] + sort[r] < tar:
                    l += 1
                elif sort[l] + sort[r] == tar:
                    res.append([sort[x], sort[l],sort[r]])
                    l += 1
                    r -= 1
                    while l < r and sort[l] == sort[l-1]:
                        l += 1


                    

        return res  