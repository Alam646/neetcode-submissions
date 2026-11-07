class Solution:
    def minWindow(self, s: str, t: str) -> str:
        min_len = float('inf')
        res = [-1, -1]  # Stores best [left, right] indices

        t_hash = {}

        for x in range(len(t)):
            if t[x] in t_hash:
                t_hash[t[x]] += 1
            else:
                t_hash[t[x]] = 1
               
        window = {}
        need = len(t_hash)
        have = 0

        left = 0

        for right in range(len(s)):
            
            if s[right] in window:
                window[s[right]] += 1
            else:
                window[s[right]] = 1

            if s[right] in t_hash and window[s[right]] == t_hash[s[right]]:
                have += 1

            
            
            while have == need:
                if min_len > right - left + 1:
                    min_len = right - left + 1
                    res = [left, right]
                
                window[s[left]] -= 1

                if s[left] in t_hash and window[s[left]] < t_hash[s[left]]:
                    have -= 1

                if window[s[left]] == 0:
                    del window[s[left]]
            
                
                left += 1

        if min_len != float('inf'):
            return s[res[0]:res[1]+1]
        else:
            return ""