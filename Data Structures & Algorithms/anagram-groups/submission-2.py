class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mainhash = {}

        for x in strs:
            key = "".join(sorted(x))
            if key in mainhash:
                mainhash[key].append(x)
            else:
                mainhash[key] = [x]
        
        return list(mainhash.values())

# Problem: Dictionaries require exact key matches, so anagram permutations like "eat", "tea", and "ate" map to separate keys.
# Core Pattern: Key Normalization
# Key Intuition: Group permutations by converting variations into a single canonical key.
#   1. Sorted String — O(N * K log K): Sort characters ("eat", "tea" -> "aet"). Easy, but sorting adds log K overhead.
#   2. Count Tuple — Optimal O(N * K): Use a 26-element tuple of letter frequencies ((1,0,0...) for 1 'a', 1 'e', 1 't'). 
#      Bypasses sorting to process each string in O(K) time, mapping all anagrams to the same bucket automatically.