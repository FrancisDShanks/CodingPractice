# 用两个栈实现,正解
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._ps = []
        self._pp = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._ps.append(x)
        
    def ps_to_pp(self):
        while self._ps:
            self._pp.append(self._ps.pop())

            
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self._pp:
            self.ps_to_pp()
        return self._pp.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self._pp:
            self.ps_to_pp()
        return self._pp[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self._ps and not self._pp
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()

# 用一个栈取了栈底元素
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._q = []
        self.size = 0

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._q.append(x)
        self.size += 1
        

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if self.size <= 0:
            return None
        p = self._q[0]
        self.size -= 1
        del(self._q[0])
        return p
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if self.size <= 0:
            return None
        return self._q[0]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.size
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
