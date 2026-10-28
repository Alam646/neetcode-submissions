class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        hash1, hash2 = {}, {}

        for x in range(len(s)):
            
            if s[x] in hash1:
                hash1[s[x]] += 1
            else:
                hash1[s[x]] = 1
            

            if t[x] in hash2:
                hash2[t[x]] += 1
            else:
                hash2[t[x]] = 1

        return hash1 == hash2    