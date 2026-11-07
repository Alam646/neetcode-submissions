class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        target = {}

        for x in range(len(s1)):
            if s1[x] in target:
                target[s1[x]] += 1
            else:
                target[s1[x]] = 1


        window = {}
        left = 0
        win_len = len(s1)

        for right in range(len(s2)):

            if s2[right] in window:
                window[s2[right]] += 1
            else:
                window[s2[right]] = 1

            if (right - left + 1) > win_len:
                window[s2[left]] -= 1 
                if window[s2[left]] == 0:
                    del window[s2[left]]
                left += 1
                
            
            if window == target:
                return True
        
        return False