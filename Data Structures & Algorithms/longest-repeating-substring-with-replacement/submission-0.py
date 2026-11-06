class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        hash = {}
        left = 0
        max_win = 0

        for right in range(len(s)):
            
            if s[right] in hash:
                hash[s[right]] += 1
            else:
                hash[s[right]] = 1

            window_len = right - left + 1
            max_freq = max(hash.values())
            replace = window_len - max_freq

            if replace <= k:
                max_win = max(max_win, window_len)
            else: 
                hash[s[left]] -= 1
                left += 1
                
        
        return max_win