# Problem: Ensuring nested or sequential elements (like brackets) perfectly resolve in the correct order.
# Core Pattern: Stack (LIFO) + Hash Map Rulebook
# Key Intuition: Open brackets are unresolved obligations. Push them onto the stack. A closing bracket must perfectly match the most recently opened obligation (top of the stack). Use a dictionary to instantly check matches and eliminate long if/else chains. If the stack is empty when a closing bracket arrives, or if items remain in the stack at the end, the string is invalid.

class Solution:
    def isValid(self, s: str) -> bool:

        # Stack tracks unresolved open brackets (Last-In, First-Out)
        stack = []

        # Rulebook mapping closing brackets (keys) to their required open brackets (values)
        dict = {')': '(', ']': '[', '}': '{'}

        # Single pass left-to-right through the string
        for i in range(len(s)):

            # 1. If the character is a CLOSING bracket
            if s[i] in dict:
                
                # Short-circuit check: Ensure stack isn't empty, THEN check if the top item is the correct match
                if stack and stack[-1] == dict[s[i]]:
                    stack.pop() # Match found! Resolve the obligation by removing it
                else:
                    return False # Mismatch (e.g., '(]') or stack is empty (e.g., ']') -> Invalid
            
            # 2. If the character is an OPEN bracket
            else:
                stack.append(s[i]) # Push it onto the stack as a new obligation

        # 3. Final validation
        # If the stack is empty, all brackets were matched. 
        # If items remain, there were unclosed open brackets (e.g., "([").
        if len(stack) == 0:
            return True
        else:
            return False