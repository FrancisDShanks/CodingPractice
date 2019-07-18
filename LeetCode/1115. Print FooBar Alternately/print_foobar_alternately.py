# can use Semaphore, Lock, Event, etc.
from threading import Semaphore
class FooBar:
    def __init__(self, n):
        self.n = n
        self.semaphore = [Semaphore(1), Semaphore(0)]

    def foo(self, printFoo: 'Callable[[], None]') -> None:     
        for i in range(self.n):
            if self.semaphore[0].acquire():
                printFoo()
                self.semaphore[1].release()               

    def bar(self, printBar: 'Callable[[], None]') -> None:    
        for i in range(self.n):
            if self.semaphore[1].acquire():
                printBar()
                self.semaphore[0].release()
