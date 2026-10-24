class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        lettercountS, lettercountT = {}, {}

        for i in range(len(s)):
            charS = s[i] # the character at the i index for string s
             # then we increment the counter for that letter
            lettercountS[charS] = 1 + lettercountS.get(charS, 0)
            
            charT = t[i] # the character at the i index for strong t
            lettercountT[charT] = 1 + lettercountT.get(charT, 0)   
        return lettercountS == lettercountT