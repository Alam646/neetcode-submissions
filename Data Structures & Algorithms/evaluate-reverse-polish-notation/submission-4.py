# Problem: Evaluate an arithmetic expression in Reverse Polish Notation where operators follow their operands.
# Core Pattern: Stack (Two-Pop Evaluation)
# Key Intuition: A stack perfectly holds intermediate values. When a number is seen, push it. When an operator is seen, pop the two most recent numbers, apply the operator (remembering the first pop is the RIGHT operand, the second is the LEFT), and push the result back onto the stack. By the end, the operations collapse the stack into a single final answer.

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        stack = [] # Stores numbers waiting to be operated on

        for x in range(len(tokens)):
            
            # Operator encountered: Pop two numbers, compute, and push the result
            if tokens[x] == "+":
                num1 = stack.pop() # The first pop is the RIGHT operand
                num2 = stack.pop() # The second pop is the LEFT operand
                res = num2 + num1
                stack.append(res)  # Push the result back to act as an operand for future operations
            
            elif tokens[x] == "-":
                num1 = stack.pop()
                num2 = stack.pop()
                res = num2 - num1
                stack.append(res)
            
            elif tokens[x] == "*":
                num1 = stack.pop()
                num2 = stack.pop()
                res = num2 * num1
                stack.append(res)
            
            elif tokens[x] == "/":
                num1 = stack.pop()
                num2 = stack.pop()
                # Python division quirk: use int(num2 / num1) to strictly truncate toward zero. 
                # Do NOT use //, because it floors toward negative infinity (e.g., 6 // -132 = -1).
                res = int(num2 / num1)
                stack.append(res)
            
            else:
                # Token is a number. Convert from string to integer and push to stack.
                int_num = int(tokens[x])
                stack.append(int_num)
        
        # After processing all tokens, the entire equation has collapsed into a single number
        return stack[0]