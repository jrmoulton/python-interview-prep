
from typing import List


class MinStack:

    def __init__(self):
        self.data: List[int] = []
        

    def push(self, val: int) -> None:
        self.data.append(val)

    def pop(self) -> None:
        self.data.pop()
        

    def top(self) -> int:
        return self.data[-1]
        

    def getMin(self) -> int:
        return min(self.data)
        
# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

def test_stack():
    my_stack = MinStack()
    my_stack.push(-11)
    my_stack.push(5)
    my_stack.push(3)
    my_stack.push(-4)
    my_stack.pop()
    assert my_stack.top() == 3
    assert my_stack.getMin() == -11
