class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        dict = {')': '(', ']': '[', '}': '{'}

        for i in range(len(s)):

            if s[i] in dict:
                if len(stack) == 0:
                    return False
                elif stack[-1] == dict[s[i]]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(s[i])


        if len(stack) == 0:
            return True
        else:
            return False
        
