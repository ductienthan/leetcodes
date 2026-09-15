class Node:
    def __init__(self, value):
        self.minValue = None
        self.previousNode = None
        self.value = value
class MinStack:

    def __init__(self):
        self.currentNode = None

    def push(self, value: int) -> None:
        node = Node(value)
        node.previousNode = self.currentNode
        currentMinValue = self.currentNode.minValue if self.currentNode is not None else None
        node.minValue = min(currentMinValue, value) if currentMinValue is not None else value
        self.currentNode = node

    def pop(self) -> None:
        node = self.currentNode
        self.currentNode = node.previousNode
        return node.value if node else None 

    def top(self) -> int:
        return self.currentNode.value if self.currentNode else None

    def getMin(self) -> int:
        return self.currentNode.minValue if self.currentNode else None


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

#optimised solution
class OptimisedMinStack:

    def __init__(self):
        self.stack = []
        self.minValue = None

    def push(self, value: int) -> None:
        if len(self.stack) == 0:
            self.minValue = value
            self.stack.append(value)
        elif value < self.minValue:
            self.stack.append(2*value-self.minValue)
            self.minValue = value
        else:
            self.stack.append(value)
 
    def pop(self) -> None:
        top = self.stack.pop()
        if top < self.minValue:
            oldMin = 2*self.minValue-top
            top = self.minValue
            self.minValue = oldMin
        return top

    def top(self) -> int:
        top = self.stack[-1] if self.stack else None
        if top is not None and top < self.minValue:
            return self.minValue
        return top

    def getMin(self) -> int:
        return self.minValue


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()