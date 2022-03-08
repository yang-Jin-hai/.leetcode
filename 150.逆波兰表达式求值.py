#
# @lc app=leetcode.cn id=150 lang=python3
#
# [150] 逆波兰表达式求值
#

# @lc code=start
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = ['+', '-', '*', '/']
        for token in tokens:
            if token in operators:
                num2, num1 = stack.pop(), stack.pop()
                stack.append(str(int(eval(num1 + token + num2))))
            else:
                stack.append(token)
        return int(stack[-1])
# @lc code=end

