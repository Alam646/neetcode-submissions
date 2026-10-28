class Solution:
    def isPalindrome(self, s: str) -> bool:
        lower = s.lower()

        new_lower = ""
        for x in range(len(lower)):
            if lower[x].isalnum():
                new_lower += lower[x]


        R = -1
        for L in range(len(new_lower)):
            if new_lower[L] != new_lower[R]:
                return False
            else:
                R += -1
        return True
        