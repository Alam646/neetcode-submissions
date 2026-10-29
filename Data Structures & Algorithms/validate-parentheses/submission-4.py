class Solution:
    def isValid(self, s: str) -> bool:

        if len(s) == 1:
            return False

        stack = []

        dict = {')': '(', ']': '[', '}': '{'}

        for i in range(len(s)):
            print(stack)
            if s[i] in dict:
                if len(stack) == 0:
                    return False
                elif stack[-1] == dict[s[i]]:
                    stack.pop()
                else:
                    return False

            else:
                stack.append(s[i])
        
        print(stack)

        if len(stack) == 0:
            return True
        else:
            return False
        
