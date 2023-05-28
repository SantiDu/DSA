# leetcode, rt 6%, mu 89%

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for i in tokens:
            try:
                stack.append(int(i))
            except ValueError:
                rhs = stack.pop()
                lhs = stack.pop()
                v = eval(f"{lhs}{i}{rhs}")
                if i == "/":
                    v = int(v)
                stack.append(v)
        return stack[0]