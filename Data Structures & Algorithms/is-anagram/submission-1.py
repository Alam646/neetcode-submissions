class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        hash = {}
        cnt = 1

        for x in s:
            if x in hash:
                hash[x] += 1
            else:
                hash[x] = cnt 
        
        for y in t:
            if y in hash:
                hash[y] += 1
            else:
                return False

        for z in hash:
            if hash[z] % 2 == 1:
                return False
               

        return True

        