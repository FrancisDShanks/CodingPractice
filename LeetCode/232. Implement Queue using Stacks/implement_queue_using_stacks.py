# 用两个栈实现,正解
# push_back 的时候,放进spush
# pop_head或者peak_head 的时候, 把spush中的都倒到spop里,取栈顶就行
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self._spush = []
        self._spop = []
        

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self._spush.append(x)
        
    def spush_to_spop(self):
        while self._spush:
            self._spop.append(self._spush.pop())

            
    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        if not self._spop:
            self.spush_to_spop()
        return self._spop.pop()
        

    def peek(self) -> int:
        """
        Get the front element.
        """
        if not self._spop:
            self.spush_to_spop()
        return self._spop[-1]
        

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self._spush and not self._spop
        


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
