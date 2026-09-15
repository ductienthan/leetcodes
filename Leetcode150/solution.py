import operator as op
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operand = {'+', '-', '*', '/'}
        operator = {
            "+": op.add,
            "-": op.sub,
            "*": op.mul,
            "/": self.divide
        }
        for token in tokens:
            if token in operand:
                second = stack.pop()
                first = stack.pop()
                stack.append(operator[token](first, second))
            else:
                stack.append(int(token))
        return stack[0]
    def divide(self, first: int, second: int) -> int:
        result = abs(first) // abs(second)
        if (first < 0) != (second<0):
            return -result
        return result
        