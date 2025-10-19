#You are given an integer n. Return all well-formed parentheses strings that you can generate with n pairs of parentheses.

#Input: n = 3
#Output: ["((()))","(()())","(())()","()(())","()()()"]



class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        #only add ( if count is less than n
        #only add ) if closed count < open
        #valid if open == closed == n 

        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return 
            
            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()

            if closedN < openN:
               stack.append(")")
               backtrack(openN, closedN + 1)
               stack.pop()

        backtrack(0,0)
        return res 


        