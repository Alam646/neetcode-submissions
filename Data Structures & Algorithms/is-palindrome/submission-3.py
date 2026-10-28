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
        
# Problem: Valid Palindrome
# Core Pattern: Opposite-End Two Pointers (Boundary Convergence)

# Key Intuition: Compare characters from outer edges moving inward (L = 0, R = len(s) - 1).
#   1. Filtered String — O(N) time & O(N) space: Build clean alphanumeric string first, then compare ends.
#   2. In-Place Pointers — Optimal O(N) time & O(1) space: Move L right and R left directly on raw string, 
#      skipping non-alphanumeric characters on the fly (`while L < R and not s[L].isalnum(): L += 1`).