#You are given an array of strings tokens that represents a valid arithmetic expression in Reverse Polish Notation.

#Return the integer that represents the evaluation of the expression.

#Input: tokens = ["1","2","+","3","*","4","-"]
#Output: 5
#Explanation: ((1 + 2) * 3) - 4 = 5

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        stack = []
        for c in tokens:
            if c == "+":
                stack.append(stack.pop() + stack.pop())
            elif c == "-":
                a, b = stack.pop(), stack.pop()
                stack.append(b-a)
            elif c == "*":
                stack.append(stack.pop() * stack.pop())
            elif c == "/":
                a, b = stack.pop(), stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(c))
                
        return stack[0]
