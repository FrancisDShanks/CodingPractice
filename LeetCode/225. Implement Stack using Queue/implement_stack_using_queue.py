# 两个思路
# 思路一
class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self._q1 = deque()
        self._q2 = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        # 把q2里面的都倒到q1去暂存
        self._q1, self._q2 = self._q2, self._q1
        # q2拿来插入最新的,然后把q1里面的都放到q2插入的新元素后面
        self._q2.append(x)
        while len(self._q1) > 0:
            self._q2.append(self._q1.popleft())
        
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        return self._q2.popleft()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        return self._q2[0]
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self._q1 and not self._q2
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()


# 思路二

class MyStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        from collections import deque
        self._q1 = deque()
        self._q2 = deque()
        

    def push(self, x: int) -> None:
        """
        Push element x onto stack.
        """
        if self._q2 and not self._q1:
            self._q1, self._q2 = self._q2, self._q1
        self._q1.append(x)
        

    def pop(self) -> int:
        """
        Removes the element on top of the stack and returns that element.
        """
        if self._q2 and not self._q1:
            self._q1, self._q2 = self._q2, self._q1
        if not len(self._q2):
            while len(self._q1) > 1:
                self._q2.append(self._q1.popleft())
        return self._q1.popleft()
        

    def top(self) -> int:
        """
        Get the top element.
        """
        if self._q2 and not self._q1:
            self._q1, self._q2 = self._q2, self._q1
        if not len(self._q2):
            while len(self._q1) > 1:
                self._q2.append(self._q1.popleft())
        tmp = self._q1[0]
        self._q2.append(self._q1.popleft())
        return tmp
        

    def empty(self) -> bool:
        """
        Returns whether the stack is empty.
        """
        return not self._q1 and not self._q2
        


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()
