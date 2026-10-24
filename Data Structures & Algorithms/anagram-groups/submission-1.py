class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagram_map = defaultdict(list)

        for s in strs:
            sorted_char = sorted(s)
            signature = "".join(sorted_char)
            anagram_map[signature].append(s)
        return anagram_map.values()
        