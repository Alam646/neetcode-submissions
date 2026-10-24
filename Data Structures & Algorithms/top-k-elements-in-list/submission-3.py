class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = {}
        for i in nums:
            if i in freq_map:
                freq_map[i] += 1
            else:
                freq_map[i] = 1

        frequency_buckets = [[] for _ in range(len(nums) + 1)]

        for i in freq_map:
            frequency = freq_map[i]
            frequency_buckets[frequency].append(i)

        res = []
        for i in range(len(frequency_buckets) - 1, 0, -1):
            bucket_freq = frequency_buckets[i]
            for j in bucket_freq:
                if len(res) < k:
                    res.append(j)
                else:
                    break
            if len(res) == k:
                break

        return res

            


