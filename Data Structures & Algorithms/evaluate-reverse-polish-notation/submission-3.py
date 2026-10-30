class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for x in range(len(tokens)):
            if tokens[x] == "+":
                num1 = stack.pop()
                num2 = stack.pop()
                res = num2 + num1
                stack.append(res)
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
                res = int(num2 / num1)
                stack.append(res)
            else:
                int_num = int(tokens[x])
                stack.append(int_num)
        
        return stack[0]