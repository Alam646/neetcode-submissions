class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        hash = {}
        
        for num in nums:

            if num in hash:
                hash[num] += 1
            else:
                hash[num] = 1

        max = 0
        pairs = []
        for num in hash:

            count = hash[num]
            pairs.append((count, num))            

        pairs.sort()
        pairs.reverse()
        
        pairs = pairs[:k]

        res = []
        for x in range(len(pairs)):
            res.append(pairs[x][1])

        return res


        #values = list(hash.values())
        #sorted = values.sort()
        #print(sorted)

        #target = hash[:k]

        return target

#Input: nums = [1,2,2,3,3,3], k = 2

#Output: [2,3]

#{1:1, 2:2, 3:3}