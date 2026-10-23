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